# PROGRESS

**Поточна фаза:** Фаза 0 — Фундамент Python та інструменти

**Де зупинились:** завершили Урок 05 (matplotlib + seaborn + Pearson correlation deep dive). Залишилось два уроки до кінця Фази 0.

## Наступний крок
Урок 06 — **Jupyter workflow**: інтерактивні notebooks як стандартне середовище для EDA і експериментів.

Мета — вивести Мартина зі "скриптового" світу (`uv run python 05_viz.py`) в notebook-workflow, який реально використовується в data-science і ML. Один notebook = один звіт з якого можна показати результати.

Теми:
- `jupyter lab` vs `jupyter notebook` vs VS Code notebook interface.
- Cells: code / markdown / raw.
- Kernel: як він тримає state, коли restart потрібен.
- Магії: `%matplotlib inline`, `%%time`, `%who`, `%%bash`.
- Порядок виконання ≠ порядок кодування — головна пастка.
- Titanic-звіт у ноутбуці: markdown-заголовки → код → графіки → висновки.
- Експорт: `.ipynb` → `.html` / `.pdf` для портфоліо.
- `.gitignore` для `.ipynb_checkpoints/`.

Урок піде в `docs/phase-0-python/06-jupyter.md`.

**Retrieval-check на старті** (з Уроку 05):
- `plt.show()` — навіщо, коли без нього ламається.
- countplot vs barplot — сформулювати різницю без cheat-list.
- Correlation ≠ causation — сформулювати confounder на новому прикладі (не bar/beer).

**Задачі-борги (перенесено з попереднього PROGRESS):**
- Виправити `import seaborn` посеред файлу у `04_pandas.py` → перенести нагору. (Треба зробити при першому ж поверненні у 04-й файл.)
- Показати `ruff format .` як autoformat-on-save для консистентного стилю.

## Пройдено
- **Урок 01** — Python basics: comprehensions, generators, decorators, context managers, type hints ([docs](docs/phase-0-python/01-python-basics.md), [memories](memories/lessons/01-01-python-basics.md))
- **Урок 02** — Type hints + mypy: `list[int]`, `str | None`, `tuple`, `dict[str, int]`, mypy --strict ([docs](docs/phase-0-python/02-type-hints.md), [memories](memories/lessons/01-02-type-hints.md), voice Feynman ✓)
- **Урок 03** — NumPy: створення масивів, shape/dtype, векторна арифметика, slicing 1D/2D через кому, broadcasting (правило справа наліво), axis=0/1, z-score normalization з sanity check ([docs](docs/phase-0-python/03-numpy.md), [memories](memories/lessons/01-03-numpy.md), voice Feynman ✓ + retrieval ✓ 2026-07-12)
- **Урок 04** — pandas: DataFrame/Series, огляд датасету (`head/info/describe`), selection (`[]`, `[[]]`, `.loc`, `.iloc`, boolean masks), groupby (три патерни), Titanic EDA через seaborn ([docs](docs/phase-0-python/04-pandas.md), [memories](memories/lessons/01-04-pandas.md)). Також: перше знайомство з `uv` як пакетним менеджером — Python-екосистема vs `brew`, CPython vs Python.
- **Урок 05** — matplotlib + seaborn: Figure/Axes state, три базові типи (histplot/countplot/boxplot), barplot з `hue` для 2D-порівняння, heatmap кореляцій; Pearson-формула під капотом (коваріація + std-нормалізація), геометрична cosine-інтуіція, обмеження на лінійні залежності, correlation ≠ causation (confounder self-derived — bar/age/beer analogy) ([docs](docs/phase-0-python/05-visualization.md), [memories](memories/lessons/01-05-visualization.md))

## План до кінця Фази 0
- **Урок 06** (наступний) — Jupyter workflow: notebooks як робоче середовище для EDA і експериментів.
- **Урок 07** — Git-for-ML: гілки, `.gitignore` для даних/моделей, LFS для великих файлів.
- **Capstone Фази 0** — самостійний EDA-звіт у Jupyter на новому датасеті (не Titanic), збережений як `.html` + запушений в окремий portfolio-репо.

Після цього паралельно стартують Фаза 1 (математика — 3Blue1Brown Essence of Linear Algebra) і Фаза 2 (класичний ML — Andrew Ng або Hands-On ML by Géron).

---

*Оновлюй цей файл після кожного уроку: перекидай завершене в "Пройдено" з посиланням, ставиш новий "Наступний крок".*
