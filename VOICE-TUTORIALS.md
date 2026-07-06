# VOICE-TUTORIALS — голосове закріплення

Додаток до [`CLAUDE.md`](./CLAUDE.md). Описує, як текстовий цикл навчання (урок у `docs/` → нотатки в `memories/`) розширюється голосовою сесією з локальним AI-агентом.

## TL;DR

Поверх кожного письмового уроку — коротка розмова голосом з агентом. Три режими:

- **Feynman** (10 хв, одразу після уроку) — я пояснюю тему агенту, що грає початківця. Ловлю в собі жаргон і провали в розумінні.
- **Retrieval** (5 хв, на старті наступної сесії) — агент ставить питання по попередньому матеріалу без підказок, коригує помилки.
- **Mock Interview** (30 хв, на закритті фази) — повноцінна технічна співбесіда.

Це не заміна тексту, а другий канал кодування знання. "Написав код" ≠ "поясню вголос під тиском".

## Навіщо (педагогіка)

| Режим | Що вирішує | Наукова база |
|---|---|---|
| **Feynman** | Метакогнітивна калібрація. "Думав, що знаю" виявляється миттєво, коли не можеш пояснити просто. | Feynman technique; Chi et al. — self-explanation effect. |
| **Retrieval** | Довгострокова пам'ять через ефект забування-і-згадування. | Roediger & Karpicke (2006), testing effect. Найсильніша окрема інтервенція для утримання. |
| **Interview** | Виступ під тиском. ML-співбесіди — на 60% вербальне пояснення концептів. | Ericsson — deliberate practice в реалістичних умовах. |

Разом закривають ланцюжок "розумію → пам'ятаю → вмію показати". Один режим — тільки третину.

## Технічна база

Голосова частина живе окремо: [`~/development/TTS-piper/voice-agent`](https://github.com/kontstantinsm1/TTS-piper) (локальний Pipecat-сервер).

**Стек:**
- STT — Deepgram (nova-3)
- LLM — OpenAI GPT-4.1
- TTS — Cartesia (sonic-3)
- Transport — WebRTC P2P (браузер ↔ localhost, без Daily/CDN)

**Запуск сесії:**

```bash
cd ~/development/TTS-piper/voice-agent && ./start-local.sh
```

Відкриваєш URL зі згенерованим flow:

```
http://127.0.0.1:8000/?flow=eli5-ua_ml-phase0-01-python-basics_feynman&autostart=1
```

URL-параметр `flow=X` підтягує `flows/X.json`, будує system prompt через `build_prompt.py`, `autostart=1` — одразу починає розмову.

## Життєвий цикл flow-файлу

1. **Створюється** — під час `/end-lesson` як draft, згенерований з розділів "Що це" / "Розбір" / "Gotchas" щойно записаного уроку в `docs/`.
2. **Ревʼю** — Claude показує 3-5 питань + follow-ups, я кажу "ок / підправ / пропусти". Без явного "ок" — не зберігається.
3. **Використовується** — файл лежить у `voice-agent/flows/`, URL — у закладках браузера.
4. **Архівується** — через місяць переїжджає у `voice-agent/flows/archive/`. Не видаляти: старі flow цінні для ретроаналізу росту.

## Naming convention

```
{mode}_ml-{phase}-{lesson-nn}-{topic-slug}_{purpose}.json
```

Приклади:
- `eli5-ua_ml-phase0-01-python-basics_feynman.json`
- `tutor-ua_ml-phase0-02-type-hints_retrieval.json`
- `tech-ua_ml-phase0_final_hard.json`

`mode` — з наявних у `voice-agent/build_prompt.py`: `eli5-ua`, `tutor-ua`, `tech-ua`.

## Personas

| Mode | Persona | Поведінка |
|---|---|---|
| `eli5-ua` | `curious_beginner` | Не знає нічого, часто перепитує "а що це значить?". Ловить нерозʼяснений жаргон і криві аналогії. |
| `tutor-ua` | `demanding_tutor` | Ставить питання, слухає, дає explicit feedback: "Правильно / Частково — помилка в X / Ні — насправді Y". Ніяких підказок наперед. |
| `tech-ua` | `hiring_manager_winwin` | Інтервʼюер. Тільки нейтральні маркери під час сесії ("Зрозумів / Далі"). Оцінка — після. |

## Приклад flow-файлу (Feynman)

```json
{
  "mode": "eli5-ua",
  "topic": "python-basics",
  "difficulty": "easy",
  "duration_min": 10,
  "language": "uk",
  "interviewer_persona": "curious_beginner",
  "opening": "Привіт! Я хочу зрозуміти, як працює Python. Ти щось про нього знаєш? Розкажи максимально просто — я новачок.",
  "questions": [
    {
      "id": "q1",
      "text": "Що таке змінна і навіщо вона потрібна?",
      "follow_ups": [
        "А чому не можна просто написати число як є?",
        "Що станеться, якщо я двом змінним дам одне імʼя?"
      ],
      "time_budget_sec": 120
    },
    {
      "id": "q2",
      "text": "Що таке функція? Поясни на прикладі з життя.",
      "follow_ups": [
        "А чому не викликати той самий код двічі замість функції?"
      ],
      "time_budget_sec": 120
    }
  ],
  "wrap_up": "Дякую! Скажи, чи було щось, що ти сам не зміг пояснити просто? — це найкорисніше, що ми знайшли."
}
```

## Правила використання

- Не робити всі три режими поспіль. Втома вбʼє ефект.
- Feynman — одразу після уроку, поки матеріал ще в короткочасній памʼяті. Якщо не встигаєш — краще завтра, ніж халявити зараз.
- Retrieval — на старті нової сесії, тільки коли нова тема будується на попередній. Не робити просто "щоб було".
- Interview — коли реально закрив цілу фазу і хочеш перевірити чи тримається в голові як цілісна картина. Не як екзамен, а як репетиція виступу.

## Roadmap

- ✅ `voice-agent` з режимами `eli5-ua`, `tutor-ua`, `tech-ua` (готове, взяте з попередніх проектів)
- 🚧 Автогенерація Feynman flow у `/end-lesson` — v1
- ⏳ Retrieval flow на старті сесії — після того, як буде ≥3 закритих уроки для розносу в часі
- ⏳ Mock Interview на закритті фази — на кінець Фази 0

## Джерела

- Roediger H., Karpicke J. (2006). *Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention.*
- Bjork R. — концепт *Desirable Difficulties*.
- Chi M. et al. (1994). *Eliciting Self-Explanations Improves Understanding.*
- Ericsson K.A. — *Deliberate Practice*, роль зворотного звʼязку.
- Feynman R. — техніка "поясни першокласнику" (усно, не в статті).
