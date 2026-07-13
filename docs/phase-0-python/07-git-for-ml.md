# Урок 07 — Git-for-ML: nbstripout, ML gitignore, LFS

## Що це

Це не "git з нуля" — ти вже знаєш базові команди (branch, commit, push, merge). Урок **про ML-специфіку git-workflow:**
- Як не роздути репо великими датасетами і моделями.
- Як тримати `.ipynb` файли чистими у git.
- Як версіонувати експерименти без "звалища" комітів.

Три конкретні навички:

1. **`.gitignore`** правильно налаштований для ML — датасети, моделі, логи експериментів, кеші.
2. **`nbstripout`** як git clean-filter — автоматичне стрипання output-ів з `.ipynb` перед комітом.
3. **Git LFS** для великих бінарників — концепція і команди, реальне використання — коли з'явиться потреба.

Плюс паттерни commit hygiene та експериментальних гілок як робочий workflow, не як setup.

## Для чого

У ML-проектах з'являються артефакти яких у бекенді не було:

- **Великі датасети** — CSV 500 МБ, паркет 5 ГБ. GitHub ліміт 100 МБ/файл + 5 ГБ на репо soft-warn. `git add data/train.csv` → репо непіддатний для клонування.
- **Треновані моделі як бінарники** — 10 МБ - 10 ГБ. Git не робить diff на бінарниках, кожна версія зберігається повністю. Модель 100 МБ × 10 комітів = 1 ГБ у історії репо.
- **`.ipynb` з embedded outputs** — base64-JSON PNG у кожному коміті. Роздуває репо, робить diff-и нечитабельними, git blame показує "все змінилось всюди" бо output re-generated щоразу.
- **Логи експериментів** — MLflow (`mlruns/`), Weights & Biases (`wandb/`), TensorBoard, PyTorch Lightning (`lightning_logs/`).
- **Кеші** — `.pytest_cache/`, `.ipynb_checkpoints/`, `__pycache__/`, HuggingFace cache.

Без правильної гігієни репо роздувається, стає повільним, коліруш стає болючим. З правильною — код і артефакти чисто розділені.

## Розбір

### 1. `.gitignore` — ML-специфіка

Три блоки додаються поверх загального Python/OS `.gitignore`:

```gitignore
# ─── ML data ────────────────────────────────────────────────────
# Датасети — велике, комітити через LFS або DVC якщо треба
data/raw/
data/processed/
data/interim/
*.parquet
*.feather
*.h5
*.hdf5

# ─── ML models & checkpoints ────────────────────────────────────
# Треновані моделі — бінарники
models/
checkpoints/
*.pkl
*.joblib
*.pt
*.pth
*.onnx
*.tflite
*.safetensors

# ─── Experiment tracking ────────────────────────────────────────
mlruns/          # MLflow
wandb/           # Weights & Biases
lightning_logs/  # PyTorch Lightning
tensorboard/     # TensorBoard
```

**Тонкий момент:** `*.csv` як glob може бути занадто широким. Якщо є маленький reference-CSV з константами (напр. `config/mappings.csv`) — його треба комітити. Тоді:

```gitignore
*.csv
!config/*.csv   # заперечення виключення — залишає ці файли у git
```

Патерн `!<path>` — це "виключення з виключення" в git glob.

**Як перевіряти що правило працює:**

```bash
git check-ignore -v data/raw/train.csv
# .gitignore:65:data/raw/    data/raw/train.csv
```

Виводить які саме `.gitignore` і рядок ловлять файл. Якщо тиша — файл не ігнорується.

### 2. `nbstripout` — clean-filter для `.ipynb`

**Проблема.** Notebook файл містить embedded PNG-графіків у base64-JSON. Розмір може досягати 100+ КБ на просте EDA. При комітах — тонни бінарних змін у diff, git blame стає нечитабельним.

**Рішення.** `nbstripout` — утиліта і git **clean-filter**. Перехоплює `.ipynb` перед комітом:
1. Читає файл.
2. Стрипає всі output-и (image data, HTML render, stderr).
3. Стрипає execution counts (`[1]`, `[2]` → `null`).
4. Комітиться "чистий" notebook — тільки код + markdown.

Локально на диску output-и залишаються (щоб було зручно працювати з графіками). Тільки git-storage бачить стриплену версію.

**Установка:**

```bash
uv add --dev nbstripout                              # dev-залежність
uv run nbstripout --install --attributes .gitattributes
```

**Критичний прапорець `--attributes .gitattributes`.** Без нього фільтр реєструється тільки в локальному `.git/config` — портативно у репо не піде. Інший розробник що клонує репо не отримає фільтр автоматично.

З ним створюється (або оновлюється) файл `.gitattributes` з:
```
*.ipynb filter=nbstripout
*.ipynb diff=ipynb
```

Цей файл комітиться у git — тому кожен хто клонує репо і має `nbstripout` встановлений отримає активний фільтр.

**Перевірка:**

```bash
git config --local --get filter.nbstripout.clean
# → /path/to/.venv/bin/python3 -m nbstripout
```

Виводить шлях до `nbstripout` у твоєму venv. Це confirmation що clean-filter зареєстровано.

**Практична перевірка на існуючому notebook:**

1. Зроби дрібну зміну у notebook (наприклад, додай пробіл в markdown-клітинці), збережи.
2. `git diff notebooks/name.ipynb | head -30`
3. Ти маєш побачити **тільки текстову зміну** — жодних base64-image діффів.

**Ефект на перший коміт після установки.** Твій наявний notebook у репо став "modified" бо clean-filter при читанні стрипає, git бачить різницю. Перший коміт після установки перетворює notebook на стриплену форму — типово це `-300 → +50` рядків (виривання outputs і execution counts).

### 3. Git LFS — коли треба комітити великі бінарники

Git не любить бінарники — кожна версія зберігається повністю (не diff-и). Модель 100 МБ × 10 версій = 1 ГБ.

**Git LFS (Large File Storage)** — розширення яке:
1. Замість зберігання бінарника в git — зберігає **pointer file** (~130 байт).
2. Реальний бінарник летить в окреме LFS-сховище (GitHub має вбудоване).
3. На pull — LFS автоматично тягне потрібну версію.

**Setup (виконуєш коли реально треба):**

```bash
# 1. Встановити git-lfs (один раз на комп'ютер)
brew install git-lfs

# 2. Ініціалізувати в поточному репо (один раз на репо)
git lfs install

# 3. Сказати LFS які файли ловити
git lfs track "*.pt" "*.h5" "*.pkl" "*.safetensors"

# 4. .gitattributes оновиться — комітимо
git add .gitattributes
git commit -m "chore: track ML models via Git LFS"

# 5. Далі просто git add model.pt → LFS перехоплює автоматично
```

**Перевірка що LFS ловить:**

```bash
git lfs ls-files      # список файлів під LFS
git lfs status        # що в staging area піде через LFS
```

**Коли LFS треба:**
- Треновані моделі які хочеш версіонувати.
- Датасети які треба зафіксувати для reproducibility (пейпер, експеримент).
- Великі PDF-звіти.

**Коли LFS НЕ треба:**
- Швидко змінні дані — краще DVC або remote storage (S3, GCS).
- Публічні датасети (Kaggle, HuggingFace) — краще завантажувати по URL через `make data`.
- Одноразові експерименти — краще W&B artifacts.

**Обмеження GitHub free tier:**
- 1 ГБ storage.
- 1 ГБ bandwidth/місяць.
- Про запас — купуєш data packs, переходиш на HuggingFace Hub / DVC + S3.

### 4. Commit hygiene для ML-експериментів

У ML легко скотитись у "звалище": один коміт "trained model, updated notebook, changed data prep, tuned hyperparameters" — неможливо потім розібрати що спрацювало.

**Правило атомарних комітів:**
- Один коміт = одна логічна зміна.
- `feat(model): add gradient boosting baseline` — окремо.
- `feat(features): add age bucketing` — окремо.
- `chore(notebook): update EDA with new plot` — окремо.

**Commit message як журнал експериментів:**

```
feat(model): xgboost with max_depth=5, n_est=200

Baseline logreg: 0.78 accuracy on val
This model: 0.83 accuracy on val (+0.05)

Features used: age (bucketed), fare_scaled, pclass, sex_encoded
Trained on: v2 of features (2026-03-11)
Time: 4 min on M1 MacBook Air
```

Через півроку `git log` — стає CV експериментів. Ти пам'ятаєш що пробував, з якими цифрами, чому не увійшло у main.

### 5. Branch strategy для експериментів

- **`main`** — тільки working code, який запускається без сюрпризів.
- **`exp/<name>`** — експериментальні гілки. Спрацювало → merge у main. Не спрацювало → залишити гілку як історичний слід.
- **`feature/<name>`** — коли додаєш конкретну фічу яка увійде у main.

Приклад дерева:

```
main
  ├── exp/xgboost-baseline       (0.83 val, деталі у commit message, deleted)
  ├── exp/nn-multiclass          (0.71 val, bad, kept for reference)
  ├── feature/age-bucketing      (merged, kept as tag)
  └── feature/ensemble           (in progress)
```

**Git worktrees** для паралельних експериментів:

```bash
git worktree add ../claude-mentor-xgboost exp/xgboost-baseline
# Створює окрему папку з тим же репо, але на іншій гілці.
# Можеш крутити один експеримент, поки другий тренується в іншому worktree.
```

### 6. DVC (Data Version Control) — опціонально, до потреби

**DVC** — окремий інструмент який робить те що git-LFS, але з фокусом на data pipelines:
- Версіонує дані з remote (S3, GCS, локальний диск).
- Описує data pipelines у YAML (як Makefile для ML).
- Автоматично detect що треба перетренувати при зміні data чи params.

Використання виправдане на командних проектах з великими даними. Для solo-навчального проекту — overkill. Знай що існує, повертайся коли будеш працювати в data-team.

## Gotchas

- **`nbstripout --install` без `--attributes` реєструє фільтр тільки локально.** Інший розробник що клонує репо не отримає фільтр. Завжди додавай `--attributes .gitattributes` для портативності.
- **Notebook показує `modified` одразу після установки nbstripout.** Це нормально: git object store містить старий файл з outputs, clean-filter стрипає при читанні → git бачить різницю. Перший коміт перетворює notebook на стриплену форму.
- **`*.csv` в `.gitignore` як glob — over-broad.** Може заблокувати reference-CSV у `config/`. Або уникай glob-у, або використовуй `!config/*.csv` як negation.
- **LFS bandwidth ліміт на GitHub free tier — 1 ГБ/місяць.** Якщо часто pull-иш моделі — швидко з'їдається. Розглядай альтернативи (HuggingFace, DVC+S3) для великих обсягів.
- **LFS pointer file без встановленого git-lfs** — при клонуванні побачиш текстовий файл з `oid` замість справжнього бінарника. Треба `git lfs install` + `git lfs pull`.
- **`.gitattributes` — це merge point** між nbstripout і LFS (обидва пишуть туди). Якщо конфлікт правил — обидва інструменти можуть не спрацювати. Перевіряй файл руками.
- **Merge conflicts у `.ipynb`** — навіть з nbstripout можуть виникнути, бо структура JSON. Резолюція болюча. Правило: **один notebook = один автор у гілці**. Якщо треба паралельна робота — розділяй notebook-и по темах.
- **`git check-ignore -v <file>`** — треба виконувати з `.gitignore` вже налаштованим. Не показує "чи буде працювати" правило що ти щойно додав але не зберіг.

## Джерела

- **Pro Git book (безкоштовна)** — https://git-scm.com/book/en/v2. Chapters 8 (Customizing Git — hooks, attributes) і 10 (Git Internals) для глибокого розуміння.
- **nbstripout GitHub** — https://github.com/kynan/nbstripout. Дока з усіма опціями, налаштування для команд, VS Code integration.
- **Git LFS docs** — https://git-lfs.com. Setup, tracking patterns, migration guide.
- **DVC documentation** — https://dvc.org/doc. Коли будеш готовий до data pipelines.
- **"How to Version Control Machine Learning Models" (MLOps)** — https://neptune.ai/blog/version-control-for-ml-models. Comparison різних підходів LFS/DVC/MLflow.
