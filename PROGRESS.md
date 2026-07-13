# PROGRESS

**Поточна фаза:** Фаза 0 — Фундамент Python та інструменти

**Де зупинились:** завершили Урок 06 (Jupyter workflow + Titanic EDA notebook). Один урок до кінця Фази 0 — Git-for-ML.

## Наступний крок
Урок 07 — **Git-for-ML**: практики версіонування у ML-проектах.

Теми:
- Гілки для експериментів (feature branches, worktrees).
- `.gitignore` для ML-специфіки: датасети (`data/raw/`), моделі (`.pkl`, `.pt`, `.h5`), логи (`mlruns/`, `wandb/`), кеші.
- **Git LFS** для великих файлів (моделі, датасети) — коли треба, як налаштувати, ліміти GitHub.
- **`nbstripout` pre-commit хук** — автоматичне очищення output-ів у `.ipynb` перед комітом. Учень вже розуміє чому це важливо (побачив diff `.ipynb` файлу).
- Commit hygiene для експериментів: атомарні коміти, `git log` як журнал експериментів.
- Опційно: DVC (Data Version Control) як альтернатива LFS для дата-версіонування.
- Практика: налаштувати `nbstripout` у `notebooks/` + пересвідчитись що новий `titanic_eda.ipynb` коміт легкий.

Урок піде в `docs/phase-0-python/07-git-for-ml.md`.

**Retrieval-check на старті** (з Уроку 06):
- Kernel state gotcha — сформулювати чому "Restart & Run All" це reproducibility-тест, а не каприз.
- Різниця notebook vs `.py` — коли який вибирати.
- Empty `.ipynb` gotcha — чому створювати тільки через UI.

**Задачі-борги (перенесено):**
- Виправити `import seaborn` посеред файлу у `04_pandas.py`.
- Показати `ruff format .` як autoformat.

## Пройдено
- **Урок 01** — Python basics ([docs](docs/phase-0-python/01-python-basics.md), [memories](memories/lessons/01-01-python-basics.md))
- **Урок 02** — Type hints + mypy ([docs](docs/phase-0-python/02-type-hints.md), [memories](memories/lessons/01-02-type-hints.md), voice Feynman ✓)
- **Урок 03** — NumPy: масиви, broadcasting, axis, z-score ([docs](docs/phase-0-python/03-numpy.md), [memories](memories/lessons/01-03-numpy.md), voice Feynman ✓ + retrieval ✓)
- **Урок 04** — pandas: DataFrame/Series, selection, groupby, Titanic EDA ([docs](docs/phase-0-python/04-pandas.md), [memories](memories/lessons/01-04-pandas.md)). Також перше знайомство з `uv`.
- **Урок 05** — matplotlib + seaborn: базові типи, barplot з hue, heatmap, Pearson correlation deep dive, confounder problem ([docs](docs/phase-0-python/05-visualization.md), [memories](memories/lessons/01-05-visualization.md))
- **Урок 06** — Jupyter workflow: kernel-state ментальна модель, notebook як звіт з markdown+code секціями, Restart & Run All як reproducibility-тест, matplotlib без plt.show(), експорт для портфоліо. Артефакт: [`notebooks/titanic_eda.ipynb`](notebooks/titanic_eda.ipynb) — публічно доступний EDA-звіт з 7 секцій + висновки ([docs](docs/phase-0-python/06-jupyter.md), [memories](memories/lessons/01-06-jupyter.md))

## План до кінця Фази 0
- **Урок 07** (наступний) — Git-for-ML: гілки, .gitignore для даних/моделей, LFS, nbstripout.
- **Capstone Фази 0** — самостійний EDA-звіт у Jupyter на **новому датасеті** (не Titanic — може бути Iris, Wine Quality, House Prices), збережений як `.html` + запушений в окремий portfolio-репо.

Після цього паралельно стартують:
- **Фаза 1 (математика)** — 3Blue1Brown Essence of Linear Algebra + похідні/градієнти.
- **Фаза 2 (класичний ML)** — Andrew Ng або Hands-On ML by Géron.

---

*Оновлюй цей файл після кожного уроку: перекидай завершене в "Пройдено" з посиланням, ставиш новий "Наступний крок".*
