import time
import random
import sys

# تحديد صحة اللاعب عند بداية اللعبة
health = 100


# 🏆 دالة تحدد نهاية مغامرة الطمع

def die():
    global health
    if health == 0:
        print_pause(
            "💀 للأسف لقد خسرت..."
            "❤️ صحتك تدمرت كليًا! 😔"
            "🎮 اللعبة خلصت يا صديقي... 😢"
        )
        check_score()


# 🔄 دالة لتحديد المتغيرات الأساسية (score, health, money) عند بدء اللعبة

def global_s_h_m():
    global score, health, money

    if "score" not in globals():
        score = 5  # تحديد النقاط الافتراضية

    if "health" not in globals():
        health = 100  # تحديد الصحة الافتراضية

    if "money" not in globals():
        money = 50  # تحديد المال الافتراضي


# 🎲 دالة لإضافة العشوائية للنقاط خلال المغامرة

def random_score():
    global score
    change = random.randint(-2, 3)  # توليد تغير عشوائي في النقاط
    score = max(
        0, score + change
    )  # ضمان عدم انخفاض النقاط تحت الصفر

    print_pause(f"⚡ الحق! نقاطك بقت {score}! 🔥")
    print_pause("🎮 نكمل نكمل... 🚀")


# 🕐 دالة لطباعة النص مع إضافة تأخير بسيط لتحسين التجربة التفاعلية

def print_pause(message):
    print(message)
    time.sleep(1.5)

# ___________________________________________________________________________

# 🏰 دالة بدء اللعبة، تعرض القوانين الأساسية وشروط الفوز


def start_game():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    while True:
        print_pause("🎩✨ أهلاً بيك في مغامرة قلعة الظلال! 🏰🔥")
        print_pause("⚠️ خلي بالك، كل خطوة هنا ممكن تغير مصيرك! 🌀💭")
        print_pause(f"💖 صحتك الحالية:")
        print_pause(f"❤️ {health}")
        print_pause(f"💰 أموالك: {money}")
        print_pause(f"⭐ نقاطك: {score}")
        print_pause("🏆 شروط الفوز:")
        print_pause("1️⃣ اجمع أكثر من 7 نقاط ⭐")
        print_pause("2️⃣ لا تخسر صحتك تمامًا ❌❤️")

# 🔄 طلب الإدخال من المستخدم لتحديد بدء المغامرة
        choice = input("🕹️ جاهز تبدأ؟ (اة/لا): ").strip().lower()
        if choice in ["اة", "اه", "y", "yes"]:
            paths()  # الانتقال إلى اختيار المسارات
        elif choice in ["لا", "n", "no"]:
            print_pause("🚪 خلاص، نستناك في مغامرة جديدة! 🔄😃")
            break


# 🚪 دالة لتحديد المسار الذي سيسلكه اللاعب في اللعبة


def paths():

    die()  # التحقق من صحة اللاعب
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🚪✨ قدامك 3 طرق تختار منهم:")
    print_pause("🔮 1️⃣ عين الحكمة - طريق الغموض والاستكشاف. 🧙‍♂️🔍")
    print_pause("⚔️ 2️⃣ السيف المنحوت - طريق القوة والمواجهة! 💥🔥")
    print_pause("🗝️ 3️⃣ المفتاح الذهبي - طريق الطمع والكنوز! 💰👑")

# 🔄 طلب الإدخال من اللاعب لاختيار الطريق المناسب
    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣/3️⃣): ").strip().lower()
        if choice in ["1", "2", "3"]:
            break

# 🔀 الانتقال إلى الغرفة المحددة بناءً على اختيار اللاعب
    if choice == "1":
        bad_room()
    elif choice == "2":
        battel_room()
    elif choice == "3":
        greed_room()

# 🏚️ دالة تمثل غرفة الغموض، حيث يواجه اللاعب لغزًا لاختبار ذكائه


def bad_room():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🚪 دخلت ممر ضيق، لا يوجد نور...🌑")
    print_pause("🏺 الحيطان عليها نقوش غريبة...")
    print_pause("تشعر وكأنها تحكي قصة مجهولة... 📜✨")
    print_pause("⚠️ لكن عليك الإجابة على السؤال قبل المتابعة...")
    print_pause("🤔")
    print_pause("📅كم شهر يحتوي على يوم 28؟🧐")
    print_pause("1️⃣ يناير ❄️")
    print_pause("2️⃣ فبراير 💙")
    print_pause("3️⃣ جميع الأشهر 🗓️")

    while True:
        choice = input("🛤️ اختار إجابتك (1️⃣/2️⃣/3️⃣): ").strip().lower()
        if choice in ["1", "2", "3"]:
            break

    if choice == "3":
        print_pause("✅ إجابة صحيحة! 🎉 حصلت على نقطة ⭐!")
        score += 1
        bad_room_2()
    else:
        print_pause("❌ إجابة خاطئة! 😔 خسرت نقطة 🔻!")
        score = max(0, score - 1)
        bad_room_2()

# 📖 دالة تمثل المرحلة الثانية من الغرفة الغامضة
# حيث يواجه اللاعب اختيارًا بين المعرفة والمغامرة


def bad_room_2():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("📖 أمامك كتاب قديم و 📦 صندوق غريب...")
    print_pause("🤔 أيهما ستختار؟ القرار بين الحكمة والمغامرة! 🔮")

    print_pause("1️⃣ تقرأ الكتاب 📜")
    print_pause("2️⃣ تفتح الصندوق 🔓")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("📖 قريت الكتاب و اكتشفت سر الخروج! 🏆✨")
        print_pause("⭐ وزدت نقطة لأنك ماهر في اكتشاف الأسرار! 🎯")
        score += 1
        print_pause("🔥 الله عليك، بتختار الصح دايماً! 👏💪")
        random_score()
        read_book()

    elif choice == "2":
        print_pause("⚠️ الصندوق كان فخ! 🐍 خرج ثعبان وأصابك! 😨")
        print_pause("💔 خسرت 20 صحة ❤️ ونقطتين للأسف 🔻")
        score = max(0, score - 2)
        health = max(0, health - 20)
        open_chest()

# 📦 دالة تمثل المرحلة التالية بعد فتح الصندوق
# حيث يواجه اللاعب لعنة سحرية تؤثر على قراراته


def open_chest():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("📦 بعد ما فتحت الصندوق ونتا بتمشي...")
    print_pause("😲 فجأة، لقيت نفسك بتعمل حركات غريبة! 🕺")
    print_pause("⏳ استنا كده!! 🤔")
    print_pause("🐍 انت اكتشفت إن الثعبان عضك... 😨")
    print_pause("✨ وفعلاً، أصابك بلعنة سحرية غامضة!")
    print_pause("💃🔥 بترقص بطريقة لا إرادية! 😵‍💫")

    print_pause("1️⃣ هتحاول تلاقي حل عشان توقف اللعنة 🧙‍♂️🔮")
    print_pause("2️⃣ هتستسلم وتحاول تكمل الطريق 🎭🚶‍♂️")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🧙‍♂️ هتلاقي شخص عجوز، ونت طلبت مساعدته و وافق... ")
        print_pause("🔸 لكنه طلب منك 15 عملة 💰")

        print_pause("1️⃣ هتدفع العملات 💸")
        print_pause("2️⃣ هتخليها معاك يمكن تحتاجها 🤔🔐")

        while True:
            choice = input("🎭 تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
            if choice in ["1", "2"]:
                break

        if choice == "1":
            print_pause("✅ تمام، انت دفعت له الفلوس 💰...")
            print_pause("🔮 وفعلاً، حررك من اللعنة! ✨")
            money = max(0, money - 15)
            print_pause("🎉 و هتزيد نقطتين! ⭐⭐")
            score += 2
            chest_end()

        else:
            print_pause("✅ تمام، ممكن تحتاجهم بعدين! 💰")
            print_pause("😓 بس انت نقصت نقطتين ⭐⭐...")
            print_pause("🔮 اللعنة بتعوقك عن الطريق!")
            score = max(0, score - 2)
            chest_end_2()

    else:
        print_pause("⚠️ تمام، بس افتكر إنك اللي هتتحمل نتيجة اختياراتك!")
        print_pause("🤔")
        print_pause("💔 بس انت نقصت 5 صحة ❤️...")
        print_pause("🔮 اللعنة بتعوقك عن الطريق!")
        health = max(0, health - 5)
        chest_end_2()

# ⚔️ المواجهة النهائية مع الوحش
# يختار اللاعب بين القتال أو التفاوض للخروج


def chest_end():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("👹 !ظهرلك وحش، وانت محتاج تحاربه! ⚔️🔥")
    print_pause("✨ لكن انت تقدر دلوقتي تحاربه لأنك وقفت اللعنة! 💪🛡️")

    print_pause("1️⃣ تحاربه عشان تخرج ⚔️")
    print_pause("2️⃣ هتتفاهم معاه بالعقل 🧠💬")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("⚔️ هتحاربه بكل قوتك، و هتتعب معاه شويه! 💥")
        print_pause("🏆 هتكسبه فعلاً و هتعرف تخرج بسلام يا بطل! 🎉")
        print_pause("😞 بس للأسف وقع منك 20 عملة 💰 وانت بتحاربه...")
        money = max(0, money - 20)
        random_score()
        check_score()

    else:
        random_score()
        print_pause("🗣️ انت دلوقتي قدام تحدي حقيقي لأنك اخترت النقاش...🤔")
        print_pause("⚠️ لو معرفتش تقنعه يتناقش معاك...")
        print_pause("🔥 الأمور هتكون أصعب! 😟")
        print_pause("🤝 وافق يتناقش معاك...")
        print_pause("🧠 لكنه طلب منك تجاوب على سؤال عشان تعدي! 💡")
        print_pause("❌ لو مجاوبتش صح، هتنقص من صحتك! ❤️🔻")

        print_pause("🕷️ كم عدد الأرجل التي يمتلكها العنكبوت؟ 🧐")
        print_pause("1️⃣ ستة 🐜")
        print_pause("2️⃣ ثمانية 🕸️")
        print_pause("3️⃣ عشرة ❌")

        while True:
            choice = input("🛤️ اختار إجابتك (1️⃣/2️⃣/3️⃣): ").strip().lower()
            if choice in ["1", "2", "3"]:
                break

        if choice == "2":
            print_pause("✅ إجابة صحيحة! زودتك نقطة ⭐!")
            score += 1
            check_score()

        else:
            print_pause("❌ إجابة خاطئة! نقصت 10 في صحتك! ❤️🔻")
            health = max(0, health - 1)

        print_pause("🧠 خدعته فعلاً بذكائك و عرفت تخرج بسلام يا بطل! 🏆🎉")
        check_score()

# 👹 المواجهة الأخيرة مع الوحش
# اللاعب لا يستطيع محاربته مباشرة بسبب اللعنة


def chest_end_2():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("👹 !ظهرلك وحش و انت محتاج تحاربه! ⚔️🔥")
    print_pause("❌ لكن للأسف، لا يمكنك محاربته الآن...")
    print_pause("🔮 اللعنة لم تتوقف بعد! 😵‍💫")
    print_pause("1️⃣ هتحاول تحاربه عشان تخرج ⚔️")
    print_pause("2️⃣ هتتفاهم معاه بالعقل 🧠💬")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("⚔️ هتحاربه بكل قوتك، و هتتعب معاه شويه! 💥")

        outcomes = [
            "🏆 انتصر المحارب! 🎉",
            "❌ خسرت المعركة! 😞",
            "😲 تعادل غير متوقع! 🤯",
            "🐉 الوحش انسحب! 😳"
        ]
        print_pause(random.choice(outcomes))

        print_pause("😓 بس للأسف وقع منك 20 عملة 💰 وانت بتحاربه... 💔")
        money = max(0, money - 20)
        random_score()
        check_score()

    else:
        random_score()
        print_pause("🧠 هو وافق يتناقش معاك...")
        print_pause("🤝 لكنه طلب منك تجاوب على سؤال عشان تعدي!")
        print_pause("❌ لو مجاوبتش صح، هتنقص صحتك! ❤️🔻")

        print_pause("🕷️ كم عدد الأرجل التي يمتلكها العنكبوت؟ 🧐")
        print_pause("1️⃣ ستة 🐜")
        print_pause("2️⃣ ثمانية 🕸️")
        print_pause("3️⃣ عشرة ❌")

        while True:
            choice = input("🛤️ اختار إجابتك (1️⃣/2️⃣/3️⃣): ").strip().lower()
            if choice in ["1", "2", "3"]:
                break

        if choice == "2":
            print_pause("✅ إجابة صحيحة! زودتك نقطة ⭐!")
            print_pause("🎉 انت دلوقتي أنهيت المهام بنجاح!")
            print_pause("🏆 اللعبة خلصت! 🚀")
            score += 1
            check_score()

        else:
            print_pause("❌ إجابة خاطئة! 😞 نقصت 10 في صحتك! ❤️🔻")
            health = max(0, health - 1)

        print_pause("🧠 خدعته فعلاً بذكائك و عرفت تخرج بسلام يا بطل! 🏆🎉")
        check_score()

# 📖 دالة تمثل قرار اللاعب بعد قراءة الكتاب
# حيث يجب أن يختار بين الاحتفاظ به أو التخلص منه


def read_book():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("📖 وانت ماشي مكمل طريقك بعد ما قرأت الكتاب...")
    print_pause("🎒 فجأة، حسيت إن الشنطة تقيلة عليك... 😓")
    print_pause("😰 بقت عبء، ومبقتش قادر تكمل! 🏋️‍♂️💦")

    print_pause("⚖️ قدامك حل...")
    print_pause("🚮 هل هترمي الكتاب اللي قريته، أو ترمي حاجة تانية؟ 🤔")

    print_pause("1️⃣ ترمي الكتاب 📚")
    print_pause("2️⃣ تخليه معاك 🎒")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("📖 انت اخترت إنك ترمي الكتاب...")
        print_pause("🤔 هل كان القرار صحيحًا؟")
        print_pause("⚠️ افتكر إن مفيش حد غيرك بيتحمل عواقب الأمور... 😬")
        print_pause("🔄 هنكتشف بعدين هل كنت هتحتاجه ولا لا! ⏳📜")
        book_end()

    else:
        print_pause("📖 انت اخترت إنك مترميش الكتاب...")
        print_pause("🤔 تفكير سليم ومنطقي! 💡")
        print_pause("⏳ هنكتشف بعدين هل كنت هتحتاجه ولا لا... 🎭🔍")
        book_end_2()

# 🚪 نهاية القصة حيث يواجه اللاعب الوحش الأخير
# عليه اتخاذ قرار مصيري للخروج


def book_end():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🚪 انت دلوقتي قدام بوابة الخروج، لكن قابلك وحش بيقولك: ")
    print_pause("👹📖 'هات الكتاب و هخرجك!'")

    print_pause("😟 للأسف، لأنك مش معاك الكتاب...")
    print_pause("🔄 هتعمله شوية مهام تانية!")
    print_pause("1️⃣ هتعمله المهام المطلوبة، بس متعرفش اي هي... 🤷‍♂️❓")
    print_pause("2️⃣ هترفض و تحاول تخرج! 💪🚀")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🔥 انت فيك روح المغامر!")
        print_pause("🎭 اخترت تعمله المهام برغم إنك مش عارف إيه هي...")
        random_score()
        print_pause("💰 المطلوب إنك هتديله 10 عملات...")
        print_pause("❤️🔻 وينقص من دمك 20 صحة!")

        while True:
            choice = input("🤝 توافق أم ترفض؟ (1️⃣/2️⃣): ").strip().lower()
            if choice in ["1", "2"]:
                break

        if choice == "1":
            print_pause("🎉 مبروك! عملت له المهام بنجاح!")
            print_pause("🏆🚪 وخرجت بأمان!")
            money = max(0, money - 10)
            health = max(0, health - 20)
            score += 1
            check_score()

        else:
            print_pause("😠 انت عنيد جداً! ولكن للأسف، الوحش أقوى منك...💀")
            print_pause("🔒 اتحبست مدى الحياة!")
            print_pause("🤔⏳ هل كان القرار يستحق المخاطرة؟")
            score = max(0, score - 1)

    else:
        print_pause("😠 انت عنيد جداً! ولكن للأسف، الوحش أقوى منك... 💀")
        print_pause("🔒 اتحبست مدى الحياة!")
        print_pause("🤔⏳ هل كان القرار يستحق المخاطرة؟")
        score = max(0, score - 1)
        check_score()

# 🚪 تحديد مصير اللاعب عند بوابة الخروج
# يجب أن يقرر بين إعطاء الكتاب أو رفضه


def book_end_2():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🚪 انت دلوقتي قدام بوابة الخروج...")
    print_pause("👹 لكن الوحش واقف في طريقك!")
    print_pause("📖 هو كمان عرف إن الكتاب معاك...")
    print_pause("😠 واصر أكتر إنه ياخده منك!")

    print_pause("1️⃣ هتديله الكتاب 🤲📜")
    print_pause("2️⃣ هترفض تديهوله 💪🚫")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🔮 فعلاً طلعت رؤيتك للمستقبل إنك تخلي الكتاب معاك صح!")
        print_pause("💡👏 وأنا بشجعك على ده!")
        print_pause("📖 انت فعلاً أديته الكتاب وخرجت بأمان! 🚪😃")
        print_pause("⭐ كسبت نقطة لأنك تستحقها! 🎉")
        score += 1
        check_score()

    else:
        print_pause("😠 انت عنيد جداً! ولكن للأسف، الوحش أقوى منك... 💀")
        print_pause("🔒 اتحبست مدى الحياة! 😞")
        print_pause("❌ هتخسر نقطة لأنك اتحبست... 🥀")
        score = max(0, score - 1)
        check_score()
# ___________________________________________________________________________


# ⚔️ دالة تمثل مواجهة اللاعب مع المحارب الحجري، حيث يقرر بين القتال أو التفاوض


def battel_room():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🏰 دخلت الساحة، وانت ماشي في القلعة...")
    print_pause("😲 فجأة، لقيت حاجة صدمتك!")
    print_pause("🗿 لقيت المحارب الحجري واقف قدامك! ⚔️🔥")
    print_pause("🤔 هل تحاربه أو تحاول تتناقش معاه؟")

    print_pause("1️⃣ تختار القتال ⚔️")
    print_pause("2️⃣ تختار النقاش 💬🧠")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        outcomes = [
            "🏆 انتصر المحارب!", "❌ خسرت المعركة!",
            "😲 تعادل غير متوقع!", "🐉 الوحش انسحب!"
        ]
        print_pause(random.choice(outcomes))
        print_pause("🔥 أديت أداء حلو، بس...")
        print_pause("💀 للأسف الوحش أصابك إصابة خطيرة! 😨")
        print_pause("❌ خسرت نقطة بسبب الإصابة! ❤️🔻")
        score = max(0, score - 1)

        print_pause("🩹 حاولت تعالج نفسك، و نجحت في ده فعلاً! 🎉")
        print_pause("🚶‍♂️ وأنت ماشي، قابلك راجل عجوز بيطلب منك المساعدة...")
        print_pause("🧓🔒 بقاله كتير هنا محبوس وبيطلب مساعدتك!")

        print_pause("1️⃣ هتساعده 🤝")
        print_pause("2️⃣ هتكمل طريقك 🚶‍♂️➡️")

        while True:
            choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
            if choice in ["1", "2"]:
                break

        if choice == "1":
            print_pause("💖 انت فعلاً شخص طيب، وبتحب الخير للغير، بس...😟")
            print_pause("👴 العجوز طلع شرير!")
            print_pause("💰❌ سرق منك 2 سكور و 5 نقود للأسف...")

            score = max(0, score - 2)
            money = max(0, money - 5)

            print_pause("⚠️خلي بالك المرة الجاية من الناس اللي بتساعدهم!")
            print_pause("🤔")
            the_reel_challenge()

    else:
        print_pause("💪 انت اخترت اختيار غريب...")
        print_pause("🔥 بس شكلك قلبك قوي، ناشف، حديد!")
        print_pause("🏃‍♂️ انت كملت طريقك ومشيت...")
        print_pause("😠 العجوز اضايق جداً!")
        print_pause("🧙‍♂️✨ ورمى عليك تعويذة سحرية غريبة!")

        print_pause("😵‍💫 شوية ولقيت نفسك بتحك في جسمك...")
        print_pause("🤯 دي التعويذة! 🦠")
        print_pause("⚠️ التعويذة خلتك عندك حساسية قوية...")
        print_pause("💉 والحل حاجة واحدة!")
        print_pause("🎒 إنك تاخد الحقنة اللي كانت معاك احتياطي...")

        print_pause("✅ وفعلاً بتاخدها...")
        print_pause("🚶‍♂️😃 وبتخف من الحساسية وبتكمل طريقك!")
        random_score()
        the_reel_challenge()

    if choice == "2":
        print_pause("💪 انت اخترت اختيار صعب على أي شخص عادي...")
        print_pause("🔥 بس عشان انت مغامر قوي!")
        print_pause("🗣️ بتحاول تتناقش مع الوحش...")
        print_pause("🤯 وفعلاً بتعرف بالعافية إنك تقنعه! 🎭")
        print_pause("🌟 انت فعلاً شخص مبهر! 👏")
        the_reel_challenge()

# دالة تمثل التحدي الحقيقي داخل القلعة


def the_reel_challenge():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🏰 وانت ماشي ومكمل في مغامرتك داخل القلعة...")
    print_pause("⚡ الأرض بتتكسر تحتك...")
    print_pause("😱 وبتقع في ممر طويل مليان شوك وفخاخ!")
    print_pause("🌀 كل ده بيقابلك وانت بتتزحلق في الممر، وبتوصل الأرض...")

    print_pause("💥 بس بتقع جامد وبتنقص 15 صحة! 🤕")
    health = max(0, health - 15)

    print_pause("👁️‍🗨️ بتحاول تشوف أنت فين وتستوعب...")
    print_pause("🌑 وبتلاقي نفسك في أوضة ضلمة! 🕵️‍♂️")
    print_pause("🚪 بس بتدور شوية شوية وبتلاقي باب مكتوب عليه:")
    print_pause("'باب الموت أو الخروج'...☠️")

    print_pause("🚪 الباب يخيرك: تدخل من الناحية اليمين أو اليسار؟")
    print_pause("⚖️ واحد فيهم هو طريق الخروج، والتاني هو النهاية! ☠️")

    print_pause("❓ هل هتختار الجزء اليمين أم اليسار؟")
    print_pause("1️⃣ اليمين")
    print_pause("2️⃣ اليسار")
    print_pause("🤔 فكر جيدًا... الاختيار لك! 🎭")

# 🔄 دالة فرعية تحدد مصير اللاعب بين النجاة أو الفشل

    def die_notdie():

        die()  # التحقق إذا فقد اللاعب صحته بالكامل
        global_s_h_m()  # تعيين المتغيرات الأساسية
        global money, health, score  # تحديد المتغيرات العامة

        return random.choice(["🚪 الخروج بأمان", "☠️ الموت"])

    result = die_notdie()

    while True:
        choice = input("🛤️ تختار ايه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        if result == "☠️ الموت":
            print_pause("☠️ لقد دخلت باب الموت يا صديقي، للأسف... 😞")
            print_pause("🎲 كان حظك سيئًا هذه المرة...")
            print_pause("😞 معلش، تتعوض في المرة الجاية!")
            print_pause("⭐ لكنك كسبت نقطة لأنك حاولت!")
            score += 1
            print_pause("💔 للأسف صحتك بتنقص 20، بس بتكمل مغامرتك! 💀🔻")
            health = max(0, health - 20)
            the_reel_challenge_2()

        elif result == "🚪 الخروج بأمان":
            print_pause("🚪 لقد دخلت باب الخروج بأمان! 🎉")
            print_pause("🏆 لقد نجحت في مهمتك الاستكشافية!")
            print_pause("✨ اللعبة تمنحك 3 نقاط لأنك محظوظ يا بطل!⭐⭐⭐")
            score += 3
            print_pause("🤔 كان حظك حلو المرادي، بس متثقش في اللعبة...")
            print_pause("💡 خلي بالك بعد كده يا مغامر!")
            the_reel_challenge_3()

    elif choice == "2":
        if result == "☠️ الموت":
            print_pause("☠️ لقد دخلت باب الموت يا صديقي، للأسف... 😞")
            print_pause("🎲 كان حظك سيئًا هذه المرة...")
            print_pause("😞 معلش، تتعوض في المرة الجاية!")
            print_pause("⭐ لكنك كسبت نقطة لأنك حاولت!")
            score += 1
            print_pause("💔 للأسف صحتك بتنقص 20، بس بتكمل مغامرتك! 💀🔻")
            health = max(0, health - 20)
            the_reel_challenge_2()

        elif result == "🚪 الخروج بأمان":
            print_pause("🚪 لقد دخلت باب الخروج بأمان! 🎉")
            print_pause("🏆 لقد نجحت في مهمتك الاستكشافية!")
            print_pause("✨ اللعبة تمنحك 3 نقاط لأنك محظوظ يا بطل!⭐⭐⭐")
            score += 3
            print_pause("🤔 كان حظك حلو المرادي، بس متثقش في اللعبة...")
            print_pause("💡 خلي بالك بعد كده يا مغامر!")
            the_reel_challenge_3()

# 🌀 دالة تمثل المرحلة الثانية من التحدي الحقيقي داخل القلعة
# حيث يواجه اللاعب متاهة غامضة يجب أن يخرج منها


def the_reel_challenge_2():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🔮 انت دلوقتي بتكمل مغامرتك...")
    print_pause("😵‍💫 وفجأة مش عارف أنت فين، ولا جيت هنا إزاي!")
    random_score()
    print_pause("🧱 بتحاول تستوعب مكانك...")
    print_pause("😨 وبتلاقي نفسك في مكان محاط بالجدران!")
    print_pause("⚠️ ديه متاهة! ازاي وصلت هنا؟ 🤔")
    print_pause("🧗‍♂️ بتحاول تتسلق الجدران، بس للأسف عالية جداً...")
    print_pause("🔀 قدامك طرق كتير، بتفضل تجربهم، تدخل طرق مختلفة...")
    print_pause("🌪️ وتحاول تخرج من المتاهة!")
    print_pause("🌀 بتحاول.. وتحاول.. لحد ما تدخل طريق، فجأة...")
    print_pause("🚧 حائط يسد كل الطرق، ويسيبلك طريقين فقط!")
    print_pause("🛑 قدامك طريقين لتكمل مغامرتك...")
    print_pause("📜 مكتوب فوق على حائطهم:")
    print_pause("🏴‍☠️ واحد منهم هياخد منك حاجة عشوائية...")
    print_pause("😬 انت متعرفهاش!")
    print_pause("😱 لازم تختار طريق من الطريقين...")
    print_pause("💭 وتنط فيه، ومتعرفش إيه اللي هيحصلك!")

    print_pause("⚖️ اليمين ولا اليسار؟")
    print_pause("1️⃣ اليمين")
    print_pause("2️⃣ اليسار")

# 🎲 دالة فرعية تحدد مصير اللاعب داخل المتاهة بطريقة عشوائية

    def random_fate():

        die()  # التحقق إذا فقد اللاعب صحته بالكامل
        global_s_h_m()  # تعيين المتغيرات الأساسية
        global money, health, score  # تحديد المتغيرات العامة

        return random.choice([
            "تنقص صحة، تزيد سكور",
            "تزيد صحة وفلوس، تنقص سكور"
        ])

    result = random_fate()

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("⚡ انت دلوقتي اخترت اليمين، ونطيت فيه!")
        print_pause("😲 ...وفجأة!")
        if result == "تنقص صحة، تزيد سكور":
            print_pause("🎲 طلع حظك في الطريق ده أنك هتنقص صحة...")
            print_pause("⭐ لكن هتزيد سكور!")
            print_pause("❤️🔻 هتنقص 10 صحة، وتزيد 3 سكور!")
            health = max(0, health - 10)
            score += 3
        elif result == "تزيد صحة وفلوس، تنقص سكور":
            print_pause("🎉 طلع حظك في الطريق ده أنك هتزيد صحة وفلوس!")
            print_pause("❌ لكن هتنقص سكور!")
            print_pause("❤️⬆️ هتزيد صحة 30، 💰⬆️ فلوس 15!")
            health += 30
            money += 15
            score = max(0, score - 1)
        battel_end()

    elif choice == "2":
        print_pause("⚡ انت دلوقتي اخترت اليسار، ونطيت فيه!")
        print_pause("😲 ...وفجأة!")
        if result == "تنقص صحة، تزيد سكور":
            print_pause("🎲 طلع حظك في الطريق ده أنك هتنقص صحة...")
            print_pause("⭐ لكن هتزيد سكور!")
            print_pause("❤️🔻 هتنقص 10 صحة، وتزيد 3 سكور!")
            health = max(0, health - 10)
            score += 3
        elif result == "تزيد صحة وفلوس، تنقص سكور":
            print_pause("🎉 طلع حظك في الطريق ده أنك هتزيد صحة وفلوس!")
            print_pause("❌ لكن هتنقص سكور!")
            print_pause("❤️⬆️ هتزيد صحة 30، 💰⬆️ فلوس 15!")
            health += 30
            money += 15
            score = max(0, score - 1)
        battel_end()

# 🚪 دالة تحدد مصير اللاعب عند مواجهة الباب الأخير
# يجب أن يقرر بين التضحية بالنقاط للخروج أو البقاء محبوسًا


def battel_end():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🚪 بعد ما دخلت الممر، لقيت قدامك باب... 😲")
    print_pause("🔑 باب الخروج، بس...")
    print_pause("😰 أنت دلوقتي خايف تفتح الباب وتخرج،")
    print_pause("بس مفيش حل قدامك تاني!")

    print_pause("⚠️ شرط عشان تخرج من الباب إنك تخسر 2 نقطة! ❌")
    print_pause("1️⃣ هتوافق ✅")
    print_pause("2️⃣ هترفض ❌")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("✅ فعلاً انت وافقت، وخسرت 2 نقطة، بس خرجت بأمان! 🎉")
        score = max(0, score - 2)
        print_pause("🏆 مبروك الخروج يا بطل! 🎊")
        check_score()

    else:
        print_pause("❌ تمام، انت اخترت أنك ترفض، بس فضلت محبوس!")
        print_pause("😬 وخسرت 3 نقاط بسبب طمعك!")
        score = max(0, score - 3)
        print_pause("🔄 تعوضها المرة الجاية، معلش! 💪😃")
        check_score()

# 🪞 دالة تمثل المرحلة الثالثة من التحدي
# يجد اللاعب نفسه في غرفة مليئة بالمرايا
# وعليه اتخاذ قرار استراتيجي للخروج


def the_reel_challenge_3():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🔍 انت دلوقتي بتكمل طريقك للاستكشاف، بس سرحت...")
    print_pause("😵‍💫 فجأة لقيت نفسك في أوضة غريبة، مش فاهم حاجة! 🤔")
    print_pause("🪞 انعكاسك في كل مكان... ديه أوضة مرايات! 😲")
    print_pause("⚠️ انت بجد دلوقتي في تحدي كبير!")

    print_pause("🚪 قدامك خيارين عشان تعرف تخرج من الأوضة ديه...")
    print_pause("🪞 يا تكسر بعض المرايا...")
    print_pause("🤯 أو تحاول تخرج بأنك تتبع انعكاساتك!")

    print_pause("1️⃣ كسر المرايات 🏚️")
    print_pause("2️⃣ اتباع الانعكاس 🔄")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🔥 انت شخص مجازف! بعد ما كسرت المراية...")
        print_pause("😲 شوفت حاجة غريبة!")
        print_pause("🚪 لقيت باب الخروج، بس...")
        print_pause("⚠️ شرط عشان تخرج من الباب إنك تخسر 2 نقطة! ❌")

        random_score()

        print_pause("1️⃣ هتوافق ✅")
        print_pause("2️⃣ هترفض ❌")

        while True:
            choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
            if choice in ["1", "2"]:
                break

        if choice == "1":
            print_pause("✅ فعلاً انت وافقت،وخسرت 2 نقطة،بس خرجت بأمان! 🎉")
            score = max(0, score - 2)
            check_score()

        else:
            print_pause("❌ تمام، انت اخترت أنك ترفض، بس فضلت محبوس!")
            print_pause("😬 وخسرت 3 نقاط بسبب طمعك!")
            score = max(0, score - 2)
            check_score()

    else:
        print_pause("🪞 انت اخترت أنك تحاول تتبع الانعكاسات والمرايات...")
        print_pause("🚶‍♂️ بتحاول تمشي وتعدي بين المرايات بحذر...")
        print_pause("✨ وفعلاً بتعرف تلاقي باب الخروج، بس... 😲")

        random_score()

        print_pause("1️⃣ هتوافق ✅")
        print_pause("2️⃣ هترفض ❌")

        while True:
            choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
            if choice in ["1", "2"]:
                break

        if choice == "1":
            print_pause("✅ فعلاً انت وافقت،وخسرت 2 نقطة،بس خرجت بأمان! 🎉")
            score = max(0, score - 2)
            check_score()

        else:
            print_pause("❌ تمام، انت اخترت أنك ترفض، بس فضلت محبوس!")
            print_pause("😬 وخسرت 3 نقاط بسبب طمعك!")
            score = max(0, score - 2)
            check_score()

# ___________________________________________________________________________

# 🎁 الغرفة الخاصة بالطمع
# يقرر اللاعب بين فتح الصندوق الذهبي أو تركه


def greed_room():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🏰 وانت ماشي في طريقك جوه القلعة للاستكشاف... وفجأة! 😲")
    print_pause("✨ لقيت نفسك في غرفة فيها صندوق ذهبي كبير!")
    print_pause("🎁 مكتوب عليه من برا 'الكنز'! 🤯")

    print_pause("🤔 هل هتفتحه؟")
    print_pause("1️⃣ هتفتحه 💎")
    print_pause("2️⃣ هتسيبه وتكمل طريقك 🚶‍♂️")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🧐 انت شخص فضولي، فيك روح المستكشف! 🌍🔍")
        print_pause("⚖️ الفضول ممكن يجي في صالحك في بعض الأحيان...")
        print_pause("🔎 لكن في بعض الحالات ممكن يكون له عواقب!")
        print_pause("🚨 للأسف المرادي الفضول جيه ضدك...")
        print_pause("😱💥 لأن الصندوق كان فخ!")
        print_pause("❌ وخسرت نقطة... 😔")

        score = max(0, score - 1)
        dreem()

    else:
        print_pause("🧐 اخترت أنك تسيبه، أنت مش فضولي خالص...")
        print_pause("👏 اتصرفت بحكمة!")
        print_pause("🔍 صح، بردو ممكن كان يضرك، القرار كان ذكي! 💡")

        random_score()
        greed_room_2()

# 🔮 دالة تمثل التحدي السحري داخل اللعبة
# حيث يواجه اللاعب جنية تمنحه فرصة مغرية
# أو يواجه مغامرة جديدة


def dreem():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🛎️ بعد ما فتحت الصندوق ولسا هتكمل طريقك... فجأة! 😲")
    print_pause("✨ لقيت نور قوي جي من وراك من ناحية الصندوق... 👀")
    print_pause("🧚‍♀️ بتبص عشان تكتشف إيه اللي حصل...")
    print_pause("🔮 لقيت جنية طالعة من الصندوق بتقولك...")
    print_pause("'أنا جنية سحرية!' 🎁")
    print_pause("'وطالعالك عشان أديك حاجة!'")
    print_pause("🚶‍♀️ هي راحت بعيد تجيب حاجة...")
    print_pause("🤔 وانت معرفش هل هتضرك أو هتنفعك...")
    print_pause("⏳ وقاعد مستني...")
    print_pause("⌛ مستني...")
    print_pause("⏰ مستني...!")
    print_pause("⚡ وفجأة! 🔑")
    print_pause("😱 لقيتها جاية عليك بتديك مفتاح خزنة!")
    random_score()
    print_pause("🚪 روحت تشوف الخزنة...")
    print_pause("🔐 بتفتحها وأنت خايف...")
    print_pause("💰 ولقىت دهب كتير، مجوهرات، أكل، وكل اللي نفسك فيه! 🎉")
    print_pause("⚠️ بس...!")
    print_pause("🏰 عشان تاخد الحاجة ديه لازم تقعد في القلعة...")
    print_pause("🔒 وتخرج يوم واحد في السنة بس!")

    print_pause("🤷 هل هتوافق؟")
    print_pause("1️⃣ هتوافق ✅")
    print_pause("2️⃣ هترفض ❌")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🏰 انت دلوقتي داخل القلعة...")
        print_pause("✨ والجنية مشيت بعد ما وافقت!")
        print_pause("💰 وفلوسك بقت 150!")
        money = 150
        print_pause("🤯 فجأة دخل عليك تاجر!")
        print_pause("🧐 انت قاعد مستغرب...")
        print_pause("😲 قام هو مقدم نفسه وقالك:")
        print_pause("'أنا تاجر بزور القلعة كل أسبوع...'")
        print_pause("'أشوف لو محتاج تشتري حاجة.'")

        print_pause("🍽️ قالك: 'أه، بس المقابل 70 عملة.' 💰")

        print_pause("🤷 هل هتوافق؟")
        print_pause("1️⃣ هتوافق ✅")
        print_pause("2️⃣ هترفض ❌")

        while True:
            choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
            if choice in ["1", "2"]:
                break

        if choice == "1":
            print_pause("🍽️ انت خدت الأكل ودفعت حقه...")
            print_pause("🤔 بس فيه حاجة غريبة!")
            money = max(0, money - 70)

            print_pause("😖 جيت تاكل الأكل...")
            print_pause("💥 حسيت إن بطنك بتوجعك!")
            print_pause("😱 شويه وبدأت تصرخ من الألم!")
            print_pause("❤️ صحتك بدأت تقل..🔻")
            health = max(0, health - 10)

            print_pause("💊 بس دورت في شنطتك، ولقيت علاج واتعالجت! 😃")
            print_pause("⚠️ لازم تخلي بالك من مصدر الأكل...")
            print_pause("🍏 ومدى صلاحيته بعد كده!")
            random_score()
            print_pause("🏰 وقضيت بقيت عمرك في القلعة...")
            print_pause("⏳ وبتخرج يوم واحد في السنة بس...")
            check_score()

        else:
            print_pause("🤔 اختيار حكيم!")
            print_pause("⚠️ عشان ممكن يكون التاجر ده شرير...")
            print_pause("😠 بس الراجل بيضايق إنك مشترتش من عنده...")
            print_pause("😱 وبيرمي عليك تعويذة!")
            print_pause("💥 انت بدأت تصرخ من كتر الألم!")
            print_pause("❤️ صحتك بدأت تقل... 🔻")

            health = max(0, health - 10)

            print_pause("💊 بتحاول تدور في شنطتك على حاجة تساعدك...")
            print_pause("🔍 وفعلاً بتلاقي!")
            print_pause("✅ بتلاقي علاج في الشنطة، وبتاخده،وفعلاً بيحسنك!😃")

            random_score()
            print_pause("🔄 ابقى بعد كده اتعامل بلطف أكتر! 😉")
            print_pause("🏰 وبتكمل بقيت حياتك في القلعة...")
            check_score()

    else:
        print_pause("🚪 فعلاً، بتختار أنك تخرج ومقعدش داخل القلعة!")
        print_pause("⚠️ يمكن تتحبس أو يحصلك مكروه...")
        print_pause("🤔 اختيار حكيم بردو! 👏")

        random_score()

        print_pause("🚶‍♂️ وأنت خارج خلاص...")
        print_pause("😱 فجأة! فخ ظهرلك، كان هيقضي عليك!")
        print_pause("🪤 فخ تاني!")
        print_pause("😨 فخ تالت!")
        print_pause("😵‍💫 فخ رابع!")
        print_pause("⚠️ أفخاخ في كل مكان في طريقك للخروج!")

        print_pause("🏰القلعة كأنها عنيدة معاك مش عايزاك تخرج تقريبًا!😨")
        print_pause("💪 أنت بتتفادى كل الفخاخ ديه، مغامر رائع بجد!")

        print_pause("🏆 وتستاهل سكور زيادة لأنك ماهر في استكشافك! 🎮")
        print_pause("🎉 واللعبة خلصت هنا يا صديقي!")

        score += 1
        check_score()


# 🔑 دالة تمثل المرحلة الثانية من غرفة الطمع
# حيث يواجه اللاعب قرارًا حول التقاط المفتاح الذهبي
# أو تركه


def greed_room_2():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🚶‍♂️ وانت مكمل طريقك بعد ما سبت الصندوق... فجأة! 😲")
    print_pause("🔑 لقيت مفتاح ذهبي على الأرض!")
    print_pause("🤔 وانت محتار دلوقتي... يا تاخده، يا تسيبه!")
    print_pause("⚖️ انت بجد في موقف مصيري، فكر كويس! 💭")
    print_pause("🎭 كل اختيار بيغير مصيرك...")

    print_pause("1️⃣ تاخده ✨")
    print_pause("2️⃣ تسيبه ❌")

    while True:
        choice = input("🛤️ تختار إيه؟ (1️⃣/2️⃣): ").strip().lower()
        if choice in ["1", "2"]:
            break

    if choice == "1":
        print_pause("🔑 تمام، انت خدت المفتاح وخليته معاك!")
        print_pause("🚶‍♂️ وانت مكمل طريقك، لقيت باب...")
        print_pause("🚪 باب كبير جدًا، ومكتوب عليه:")
        print_pause("🧠 'حل اللغز لتخرج...'")
        print_pause("😨 'ولو محلتش، هتفضل محبوس مدى الحياة!'")

        print_pause("🍏 رجل لديه 5 تفاحات، ويريد توزيعها")
        print_pause("❓ كيف يمكنه فعل ذلك؟")

        print_pause("1️⃣ لا يمكن ذلك ❌")
        print_pause("2️⃣ يعطي كل شخص تفاحة، ويُبقي اثنتين لنفسه 🍏🍏")
        print_pause("3️⃣ يستبدلها بـ 6 تفاحات ثم يوزعها 🔄🍏")

        random_score()

        while True:
            choice = input("🛤️ اختار إجابتك (1️⃣/2️⃣/3️⃣): ").strip().lower()
            if choice in ["1", "2", "3"]:
                break

        if choice == "1":
            print_pause("✅ إجابة صحيحة! زودتك نقطة! 🎉")
            score += 1

            print_pause("🚪 بعد الإجابة، ظهر باب جديد...")
            print_pause("🔑 وبتلاحظ إنه فيه مكان للمفتاح اللي معاك!")

            print_pause("🛠️ بتجرب تحطه...✨")
            print_pause("🏰 والباب بيتفتح فعلاً، وبتخرج بسلام! 🎊")

            greed_end()

        else:
            print_pause("❌ إجابة خاطئة! نقصت نقطة! 😔")
            score = max(0, score - 1)

            print_pause("🚪 الباب متفتحش، بس فيه طريقة تانية...")
            print_pause("🔑 وبتلاحظ فجأة إن المفتاح اللي معاك ينفع! 🛠️")
            print_pause("✨ والباب بيتفتح، وبتخرج من القلعة بسلام! 🏰🎊")

            greed_end()

    else:
        print_pause("😱 سبت المفتاح ولسا هتكمل طريقك... وفجأة!")
        print_pause("🌍 الأرض اختفت تحتك! 😲")

        random_score()

        print_pause("💥 وقعت في حفرة عميقة، واتجرحت جرح شديد! 😰")
        print_pause("🆘 للأسف مفيش حد يساعدك...")
        print_pause("🤕 بتنزف بشدة...🩸")

        print_pause("❤️ صحتك نقصت 20 بسبب النزيف... 🔻")
        print_pause("🚪 و... اتحبست للأبد... 😨")

        score = max(0, score - 1)
        health = max(0, health - 20)

        greed_end_2()

# 🏆 نهاية مغامرة الطمع
# اللاعب يواجه تحديات أخيرة قبل الخروج من القلعة


def greed_end():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🦸‍♂️ فعلاً، بتخرج بذكائك خارج القلعة! 👏")
    print_pause("🤔 اختيار حكيم بردو! 💡")

    random_score()

    print_pause("🚶‍♂️ وأنت خارج خلاص...")
    print_pause("😱 فجأة! فخ ظهرلك، كان هيقضي عليك! ⚠️")
    print_pause("🪤 ايه ده! فخ تاني! فخ تالت! فخ رابع! 🤯")
    print_pause("🏰 القلعة كأنها عنيدة معاك، مش عايزاك تخرج تقريبًا!")

    print_pause("💪 انت بتتفادى كل الفخاخ ديه، مغامر رائع بجد! 🔥")
    print_pause("🏆 وتستاهل سكور زيادة لأنك ماهر في استكشافك! 🎉")
    print_pause("🎮 واللعبة خلصت هنا يا صديقي! 🏁")

    score += 1
    check_score()


# 🔮 سيناريو آخر لنهاية المغامرة
# اللاعب يحاول استخدام التعويذة للخروج

def greed_end_2():

    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية
    global money, health, score  # تحديد المتغيرات العامة

    print_pause("🔎 بتحاول تدور على طريقة للخروج، بس مش بتعرف... 😟")
    print_pause("💡 فجأة، بتفتكر التعويذة اللي معاك في الشنطة! ✨")
    print_pause("🧙‍♂️ وبتحاول تستخدمها عشان تطلع... 🔮")

    greed_end()
    check_score()


# 🏆 دالة لفحص النقاط بعد انتهاء المغامرة، وتحديد النتيجة النهائية


def check_score():

    global score, health, money
    die()  # التحقق إذا فقد اللاعب صحته بالكامل
    global_s_h_m()  # تعيين المتغيرات الأساسية

    print_pause("اللعبه انتهت يا صديقي")
    print_pause(
        f"💖 صحتك الحالية: ❤️ {health}, "
        f"💰 أموالك: {money}, "
        f"⭐ نقاطك: {score}"
                )

    if score >= 7:
        print_pause("🎉 مبروك! فزت بالمغامرة!")
    elif score < 4:
        print_pause("😢 خسرت بالمغامرة، النقاط قليلة جدًا!")
    else:
        print_pause("😃 أداء جيد، لكن تحتاج لمزيد من الحظ!")

    restart_game()


# 🔄 دالة لإعادة تشغيل اللعبة إذا أراد اللاعب تجربة مغامرة جديدة


def restart_game():

    while True:
        choice = input("(اة/لا)عايز تعيد وتجرب حاجة مختلفة؟").strip().lower()
        if choice in ["اة", "اه", "y", "yes"]:
            start_game()
        elif choice in ["لا", "n", "no"]:
            print_pause("شكرًا للعب! نتمنى أن تعود قريبًا. 😊")
            sys.exit()
        else:
            restart_game()


start_game()
