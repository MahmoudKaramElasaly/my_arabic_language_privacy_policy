import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's completely redesign the CSS and the Arabic section to make it look great for an app store.

new_style = """
      @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
      
      body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        background-color: #f0f4f8;
        color: #333;
        margin: 0;
        padding: 20px 10px;
      }
      .container {
        max-width: 900px;
        margin: auto;
        background: #fff;
        padding: 40px 30px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
      }
      .lang-switch {
        text-align: center;
        margin-bottom: 40px;
      }
      .lang-switch a {
        display: inline-block;
        padding: 12px 24px;
        background: #3498db;
        color: #fff;
        text-decoration: none;
        border-radius: 8px;
        margin: 0 10px;
        font-weight: bold;
        transition: all 0.3s ease;
      }
      .lang-switch a:hover {
        background: #2980b9;
        transform: translateY(-2px);
      }
      .section-en {
        direction: ltr;
        text-align: left;
        border-bottom: 3px solid #eee;
        padding-bottom: 40px;
        margin-bottom: 40px;
      }
      .section-ar {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
      }
      
      /* Beautiful App Title */
      .app-title-container {
        text-align: center;
        margin: 20px 0 40px 0;
        padding: 30px;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(30, 60, 114, 0.3);
      }
      
      .app-title-ar {
        font-family: 'Cairo', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        color: #ffffff;
        margin: 0;
        text-shadow: 2px 4px 8px rgba(0,0,0,0.2);
        letter-spacing: 1px;
      }
      
      .app-subtitle {
        color: #e0e0e0;
        font-size: 1.2rem;
        margin-top: 10px;
        font-weight: 400;
      }

      h1.policy-title,
      h2 {
        color: #2c3e50;
      }
      h1.policy-title {
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        display: inline-block;
      }
      .section-ar h1.policy-title {
        font-family: 'Cairo', sans-serif;
        font-weight: 700;
      }
      .section-ar h2 {
        font-family: 'Cairo', sans-serif;
        font-weight: 700;
        color: #1e3c72;
        margin-top: 30px;
      }
      a {
        color: #3498db;
        text-decoration: none;
        font-weight: bold;
      }
      a:hover {
        text-decoration: underline;
      }
      ul {
        padding-inline-start: 20px;
      }
      .section-ar ul {
        padding-inline-end: 20px;
        padding-inline-start: 0;
      }
      .section-ar li {
        margin-bottom: 10px;
      }
      .contact-email {
        color: #e74c3c;
        font-weight: bold;
        font-size: 1.1em;
      }
"""

# Replace styles
content = re.sub(r'<style>.*?</style>', f'<style>\n{new_style}\n    </style>', content, flags=re.DOTALL)

# Update English section mention of the app
content = content.replace("<strong>العربية لغتي</strong> app", "<strong>العربية لغتي (Arabic is My Language)</strong> app")

# completely rewrite the Arabic Section
arabic_section_html = """
      <!-- Arabic Section -->
      <div id="arabic" class="section-ar">
        <div class="app-title-container">
          <h1 class="app-title-ar">العربية لغتي</h1>
          <div class="app-subtitle">تطبيقك الأول لتعلم وممارسة اللغة العربية</div>
        </div>
        
        <h1 class="policy-title">سياسة الخصوصية</h1>
        <p><strong>تاريخ السريان:</strong> 14 مارس 2026</p>
        <p>
          تنطبق سياسة الخصوصية هذه على تطبيق
          <strong>العربية لغتي</strong> للأجهزة المحمولة. تُستخدم هذه الصفحة
          لإعلام الزوار والمستخدمين بسياساتنا المتعلقة بجمع المعلومات الشخصية واستخدامها
          والكشف عنها لأي شخص يقرر استخدام خدمتنا، وذلك لضمان التوافق التام مع
          سياسات بيانات المستخدمين الخاصة بمتجر جوجل بلاي (Google Play User Data Policy) ومتاجر التطبيقات الأخرى.
        </p>

        <h2>1. جمع المعلومات واستخدامها</h2>
        <p>
          للحصول على تجربة أفضل أثناء استخدام تطبيق <strong>العربية لغتي</strong>، قد نطلب منك تزويدنا
          بمعلومات شخصية معينة لتحسين تجربة التعلم. سيتم الاحتفاظ بالمعلومات التي نطلبها واستخدامها
          فقط كما هو موضح في سياسة الخصوصية هذه، وبأعلى معايير الأمان.
        </p>
        <p>
          يستخدم التطبيق خدمات تابعة لجهات خارجية قد تجمع معلومات تستخدم لتحديد
          هويتك لغرض تحسين الخدمة وتأمين حسابك. يمكنك مراجعة سياسة الخصوصية الخاصة بمقدمي الخدمات:
        </p>
        <ul>
          <li>
            <a href="https://policies.google.com/privacy" target="_blank"
              >خدمات جوجل بلاي (Google Play Services)</a
            >
          </li>
          <li>
            <a href="https://auth0.com/privacy" target="_blank"
              >خدمات تسجيل الدخول والمصادقة (Auth0)</a
            >
          </li>
        </ul>

        <h2>2. بيانات السجل (Log Data) وتقارير الأعطال</h2>
        <p>
          نريد إعلامك بأنه كلما استخدمت تطبيق <strong>العربية لغتي</strong>، وفي حالة حدوث مشكلة أو خطأ، 
          نقوم بجمع بيانات ومعلومات (من خلال منتجات جهات خارجية) على
          هاتفك تسمى Log Data. قد تتضمن هذه البيانات معلومات مثل عنوان بروتوكول
          الإنترنت ("IP") لجهازك، واسم الجهاز، وإصدار نظام التشغيل، وتكوين
          التطبيق عند استخدام خدمتنا، ووقت وتاريخ استخدامك، وإحصاءات أخرى
          بهدف إصلاح الأعطال وتحسين أداء التطبيق بشكل مستمر.
        </p>

        <h2>3. الأمان (Security)</h2>
        <p>
          نحن نقدر ثقتك الكبيرة في اختيار تطبيق <strong>العربية لغتي</strong> وتزويدنا بمعلوماتك، وبالتالي فإننا نسعى جاهدين
          لاستخدام وسائل صارمة وموثوقة لحمايتها. ولكن تذكر أنه لا توجد طريقة نقل
          عبر الإنترنت أو طريقة تخزين إلكتروني آمنة بنسبة 100٪، ولا يمكننا ضمان
          أمنها المطلق، رغم التزامنا بأفضل الممارسات البرمجية.
        </p>

        <h2>4. خصوصية الأطفال (Children’s Privacy)</h2>
        <p>
          تطبيق <strong>العربية لغتي</strong> آمن للاستخدام، ومع ذلك، نحن لا نتعمد جمع معلومات شخصية أو حساسة من الأطفال دون سن 13
          عامًا دون موافقة. في حالة اكتشافنا أن طفلاً دون سن 13 عامًا قد زودنا بمعلومات
          شخصية، فإننا نقوم بحذفها على الفور من خوادمنا. إذا كنت والدًا أو وصيًا
          وكنت على علم بأن طفلك قد زودنا بمعلومات شخصية، يرجى الاتصال بنا حتى
          نتمكن من اتخاذ الإجراءات اللازمة.
        </p>

        <h2>5. التغييرات على سياسة الخصوصية</h2>
        <p>
          قد نقوم بتحديث سياسة الخصوصية الخاصة بنا من وقت لآخر لمواكبة التطورات. وبالتالي، ننصحك
          بمراجعة هذه الصفحة بشكل دوري. سنخطرك بأي تغييرات
          عن طريق نشر سياسة الخصوصية الجديدة المشارة هنا.
        </p>

        <h2>6. تواصل معنا (Contact Us)</h2>
        <p>
          إذا كان لديك أي أسئلة أو استفسارات أو اقتراحات حول سياسة الخصوصية الخاصة بتطبيق <strong>العربية لغتي</strong>، 
          يسعدنا تواصلك معنا على:
        </p>
        <ul>
          <li>
            <strong>البريد الإلكتروني:</strong>
            <span class="contact-email">mahmoudkaramelasaly@gmail.com</span>
          </li>
        </ul>
      </div>
"""

content = re.sub(r'<!-- Arabic Section -->.*</div>\s*</div>\s*</body>', arabic_section_html + '\n    </div>\n  </body>', content, flags=re.DOTALL)
content = content.replace('<h1>Privacy Policy</h1>', '<h1 class="policy-title">Privacy Policy</h1>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
