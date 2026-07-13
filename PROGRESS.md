# PROGRESS

**Поточна фаза:** Фаза 0 ✅ **completed** → Фази 1+2 паралельно (наступне)

**Де зупинились:** усі 7 уроків Фази 0 пройдено. Наступний крок — **старт Фаз 1+2 паралельно**.

## Наступний крок — Фази 1+2 паралельно

**Рішення від 2026-07-13:** пропускаємо синтетичний capstone (Iris/Wine/House Prices тощо). Причина: практика-датасети виглядають як junior-signal, не диференціюють у portfolio. Реальний portfolio-об'єкт народиться природно у Фазі 2 коли будемо застосовувати класичний ML до **реальних задач** — agro (LoRa greenhouse monitoring), персональні дані, або справжня Kaggle-змагання з leaderboard.

**Learning-артефакт для процесу:** сам репо `claude-mentor` (7 уроків, docs, code, Titanic notebook як приклад workflow) — це вже свідчення структурованого підходу. Не виносити Titanic в окремий портфоліо-репо.

### Фаза 1 — Математика для ML (4-6 тижнів)

- **3Blue1Brown "Essence of Linear Algebra"** — YouTube playlist, 15 епізодів по 10-15 хв. Вектори, матриці, лінійні перетворення, власні значення. Візуальний, інтуїтивний.
- **Похідні + градієнти + chain rule** — основа backpropagation. 3Blue1Brown "Essence of Calculus" перші 6 епізодів.
- **Ймовірності і статистика** — розподіли, matematичне сподівання, дисперсія, Байєс. StatQuest на YouTube (Josh Starmer) для інтуїції.
- **Градієнтний спуск руками на NumPy** — реалізувати з нуля, побачити як воно збігається.
- **Функції втрат** — MSE, cross-entropy. Що вони означають геометрично.

Ресурси: 3Blue1Brown (YouTube), StatQuest, безкоштовна книга "Mathematics for Machine Learning" (Deisenroth) для довідки. Khan Academy для прогалин.

### Фаза 2 — Класичний ML (6-8 тижнів)

- **sklearn основи** — train/test split, pipelines, transformers.
- **Лінійна регресія** — з нуля на NumPy, потім через sklearn.
- **Логістична регресія** — класифікація.
- **Дерева, Random Forest** — non-parametric методи.
- **Gradient Boosting** — XGBoost / LightGBM.
- **KNN, SVM, Naive Bayes**.
- **Метрики** — precision/recall, F1, ROC-AUC, confusion matrix. Коли яку.
- **Крос-валідація, регуляризація** (L1/L2).
- **Feature engineering** — encoding категорних (one-hot, target, ordinal), scaling, feature importance.
- **Гіперпараметри** — GridSearch, RandomSearch, Optuna.

Ресурси: **"Hands-On Machine Learning"** (Aurélien Géron, 3rd ed) — ключова книга. **Andrew Ng "Machine Learning Specialization"** (Coursera) для інтуїції. sklearn docs для reference.

### Як їх чергувати

Мета — тримати обидві активними, не жертвувати однією заради іншої.

**Пропонована структура (можна коригувати):**
- **Понеділок / середа / п'ятниця** — Фаза 1 (математика). 45-60 хв: одне 3Blue1Brown відео + власна нотатка про що зрозумів.
- **Вівторок / четвер** — Фаза 2 (ML практика). 60-90 хв: sklearn урок з Géron + маленький expериментальний notebook.
- **Субота (опційно)** — інтеграція: перевір як математика тижня застосовується у практиці тижня. Або короткий проект.

**Головне правило:** якщо математика заблокована (не зрозуміло щось з калькулюсу) — **не зупиняй практику ML**. Математика підтягнеться в контексті. Andrew Ng саме так і будував свій курс.

### Retrieval-check при першому уроці кожної фази

**Фаза 1 (математика) — старт:**
- **NumPy broadcasting** — сформулювати правило справа наліво без підказки. Це буде основа роботи з тензорами скрізь.
- **`axis` семантика** — на shape (3, 4) що робить `sum(axis=0)` і чому. Це прокинеться при роботі з матричним множенням.
- **Z-score інтерпретація** — не min-max scaling, це centered + scaled (третій раз, борг з Уроку 03).

**Фаза 2 (класичний ML) — старт:**
- **EDA методологія** — три мети (якість → гіпотези → sanity). Із Уроку 04 (Feynman зупинявся на "знайомство з даними").
- **Correlation ≠ causation** — сформулювати confounder на новому прикладі (не bar/beer, не fare/pclass). Із Уроку 05.
- **notebook vs .py вибір** — прочитати завдання "тренуємо модель у cron" і сказати які файли робити в чому.

## Пройдено — Фаза 0

- **Урок 01** — Python basics ([docs](docs/phase-0-python/01-python-basics.md), [memories](memories/lessons/01-01-python-basics.md))
- **Урок 02** — Type hints + mypy ([docs](docs/phase-0-python/02-type-hints.md), [memories](memories/lessons/01-02-type-hints.md), voice Feynman ✓)
- **Урок 03** — NumPy ([docs](docs/phase-0-python/03-numpy.md), [memories](memories/lessons/01-03-numpy.md), voice Feynman ✓ + retrieval ✓)
- **Урок 04** — pandas + Titanic EDA ([docs](docs/phase-0-python/04-pandas.md), [memories](memories/lessons/01-04-pandas.md)). Перше знайомство з `uv`.
- **Урок 05** — matplotlib + seaborn + Pearson correlation + confounder problem ([docs](docs/phase-0-python/05-visualization.md), [memories](memories/lessons/01-05-visualization.md))
- **Урок 06** — Jupyter workflow + Titanic EDA notebook ([docs](docs/phase-0-python/06-jupyter.md), [memories](memories/lessons/01-06-jupyter.md)). Артефакт: [`notebooks/titanic_eda.ipynb`](notebooks/titanic_eda.ipynb).
- **Урок 07** — Git-for-ML: nbstripout, ML gitignore, LFS/branching (deferred to Фази 2 коли з'явиться реальна модель) ([docs](docs/phase-0-python/07-git-for-ml.md), [memories](memories/lessons/01-07-git-for-ml.md))

## Portfolio-об'єкти (що народиться пізніше, природно)

Не робимо синтетичні capstone-и. Реальні portfolio-piece з'являться коли:

1. **ML на agro** — anomaly detection на температуру/вологість, або прогноз коли треба провітрити. Коли зберешся достатньо даних з реальних теплиць. Домейн-експертиза + hardware + software = сильний сигнал.
2. **ML на власних даних** — trading history, gym progress, GitHub-репо аналіз, будь-що персональне. Головне — питання яке ти сам хочеш відповісти.
3. **Kaggle competition з реальним leaderboard-фінішем** — не просто "скачав датасет", а серйозна конкуренція.

Ці об'єкти виникнуть на маркерах Фази 2 (перша модель, feature engineering, hyperparameter tuning) — тоді ж і відкриємо `exp/` гілки та LFS з Уроку 07.

---

*Оновлюй цей файл після кожного уроку: перекидай завершене в "Пройдено" з посиланням, ставиш новий "Наступний крок".*
