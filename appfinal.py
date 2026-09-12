import streamlit as st
import math

# ============================================================
# GRAM SAHAYAK
# Business & Financial Guidance for Rural Micro-Entrepreneurs
# ============================================================

st.set_page_config(
    page_title="Gram Sahayak",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        background: #f7faf7;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .hero {
        padding: 1.5rem 1.8rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #eef8ef, #f8fbf5);
        border: 1px solid #dbeadd;
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.3rem;
    }

    .hero p {
        font-size: 1.15rem;
        color: #4b5563;
    }

    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.15rem;
        margin-bottom: 1rem;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    }

    .recommendation {
        background: linear-gradient(135deg, #f0f8f1, #ffffff);
        border-left: 6px solid #2e7d32;
        border-radius: 14px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }

    .score {
        font-size: 1.8rem;
        font-weight: 700;
    }

    .small-note {
        color: #6b7280;
        font-size: 0.88rem;
    }

    .tag {
        display: inline-block;
        padding: 0.3rem 0.65rem;
        border-radius: 999px;
        background: #eef6ff;
        margin-right: 0.35rem;
        font-size: 0.82rem;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        padding: 2rem 0 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# TRANSLATIONS
# -----------------------------
TEXT = {
    "English": {
        "language": "Language", "location": "Market Location", "navigate": "Navigate",
        "home": "Home", "market": "Market Prices", "schemes": "Government Schemes",
        "finance": "Financial Assistant", "business": "Business Recommendation",
        "welcome": "Welcome to Gram Sahayak",
        "subtitle": "Business & Financial Guidance for Rural Micro-Entrepreneurs",
        "home_desc": "A simple digital assistant designed to help rural micro-entrepreneurs explore local business opportunities, understand sample market conditions, estimate finances and discover relevant government schemes.",
        "crops": "Crops Covered", "locations": "Locations", "schemes_count": "Schemes",
        "business_models": "Business Models", "selected_market": "Selected Market",
        "demo_market": "Current demonstration market", "market_disclaimer": "Market prices shown in this prototype are sample data and are not live mandi/API prices.",
        "what_can": "What you can do", "explore": "Explore Markets", "explore_desc": "Compare sample prices across a wider set of crops and locations.",
        "plan": "Plan Finances", "plan_desc": "Estimate profit, revenue, costs and loan EMI before making a decision.",
        "find": "Find a Business", "find_desc": "Get a structured business shortlist based on capital, resources, interests and location.",
        "how": "How Gram Sahayak Works", "how_desc": "Your inputs → local context → rule-based business matching → financial planning → relevant scheme suggestions → practical next steps.",
        "market_title": "Market Prices", "market_desc": "Sample market information for **{location}**. Use it for demonstration and planning only; verify current local mandi prices before making financial decisions.",
        "filter": "Filter by crop category", "all": "All", "board": "Crop Market Board", "showing": "Showing {count} crops for the selected demonstration market: {location}",
        "selected_crop": "Selected Crop", "choose_crop": "Choose a crop", "crop": "Crop", "sample_price": "Sample Price", "trend": "Trend",
        "increasing": "Increasing", "stable": "Stable", "decreasing": "Decreasing",
        "market_note": "Important: location factors and prices are controlled demonstration data, not live market feeds.",
        "scheme_title": "Government Schemes", "scheme_desc": "Explore schemes that may be relevant to rural entrepreneurs, farmers, vendors, food processors and artisans.",
        "search": "Search schemes", "placeholder": "Example: food, loan, farmer, artisan", "best_for": "Best for",
        "key": "Key information", "why": "Why it may help", "source": "Official source",
        "scheme_warning": "Scheme eligibility, loan approval, subsidy availability and applicable conditions depend on the official guidelines and the applicant's circumstances. Verify details through the relevant Government of India/state portal or bank before applying.",
        "finance_title": "Financial Assistant", "profit_tab": "📊 Profit Calculator", "emi_tab": "🏦 Loan EMI Calculator",
        "profit_est": "Profit Estimator", "quantity": "Quantity", "purchase": "Purchase cost per unit", "selling": "Selling price per unit",
        "other": "Other costs", "total_cost": "Total Cost", "revenue": "Revenue", "profit": "Estimated Profit",
        "positive": "This example produces a positive estimated profit.", "break_even": "This example is approximately at break-even.",
        "loss": "This example produces an estimated loss. Review price and costs.",
        "loan": "Loan amount", "rate": "Annual interest rate (%)", "period": "Loan period (years)", "monthly": "Monthly EMI",
        "total_payment": "Total Payment", "interest": "Total Interest", "loan_note": "Actual loan terms, interest rates, fees and approval depend on the lender.",
        "business_title": "Business Recommendation", "business_desc": "Tell Gram Sahayak about your situation. The prototype will score business models using capital, resources, interest, water availability, experience and location.",
        "capital": "💰 Available capital (₹)", "resource": "🧰 Main available resource", "interest_input": "❤️ Main business interest",
        "water": "💧 Water availability", "experience": "🎯 Your experience", "good": "Good", "limited": "Limited",
        "not_applicable": "Not applicable", "not_sure": "Not sure", "beginner": "Beginner", "some": "Some experience", "experienced": "Experienced",
        "location_note": "📍 Recommendation will be adjusted for the selected market: **{location}**",
        "generate": "🔍 Generate Business Recommendations", "three": "Here are the three strongest prototype matches for your inputs.",
        "match": "Match", "investment": "Indicative investment", "model": "Business model", "why_match": "Why this matches",
        "risk": "Key risk", "steps": "Suggested first steps", "relevant": "Potentially relevant schemes",
        "next_action": "📌 Suggested next action", "below": "Your current capital is below the typical starting range for **{business}**. Consider a smaller pilot, savings, eligible financing or a lower-capital business model.",
        "next": "A practical next step is to prepare a simple cost sheet for **{business}** and compare it with expected local demand before investing.",
        "limit": "Prototype limitation: this is a rule-based recommendation engine using demonstration business profiles. It is not a live AI model and does not guarantee profitability.",
        "footer": "🌾 Gram Sahayak • Prototype for rural micro-entrepreneur business guidance",
        "footer_note": "Demo market data • Rule-based recommendations • Verify official scheme information before decisions",
    },
    "Hindi": {
        "language": "भाषा", "location": "बाज़ार स्थान", "navigate": "नेविगेट करें",
        "home": "होम", "market": "बाज़ार भाव", "schemes": "सरकारी योजनाएँ", "finance": "वित्तीय सहायक", "business": "व्यवसाय सुझाव",
        "welcome": "ग्राम सहायक में आपका स्वागत है", "subtitle": "ग्रामीण सूक्ष्म उद्यमियों के लिए व्यवसाय और वित्तीय मार्गदर्शन",
        "home_desc": "ग्रामीण सूक्ष्म उद्यमियों को स्थानीय व्यवसाय के अवसर समझने, नमूना बाज़ार स्थिति देखने, वित्त का अनुमान लगाने और उपयोगी सरकारी योजनाएँ खोजने में मदद करने वाला डिजिटल सहायक।",
        "crops": "शामिल फसलें", "locations": "स्थान", "schemes_count": "योजनाएँ", "business_models": "व्यवसाय मॉडल",
        "selected_market": "चयनित बाज़ार", "demo_market": "वर्तमान प्रदर्शन बाज़ार", "market_disclaimer": "इस प्रोटोटाइप में दिखाए गए बाज़ार भाव नमूना डेटा हैं और लाइव मंडी/API भाव नहीं हैं।",
        "what_can": "आप क्या कर सकते हैं", "explore": "बाज़ार देखें", "explore_desc": "अलग-अलग फसलों और स्थानों के नमूना भावों की तुलना करें।",
        "plan": "वित्त की योजना बनाएं", "plan_desc": "निर्णय लेने से पहले लाभ, राजस्व, लागत और ऋण EMI का अनुमान लगाएं।",
        "find": "व्यवसाय खोजें", "find_desc": "पूंजी, संसाधन, रुचि और स्थान के आधार पर व्यवसायों की सूची पाएं।",
        "how": "ग्राम सहायक कैसे काम करता है", "how_desc": "आपकी जानकारी → स्थानीय संदर्भ → नियम-आधारित व्यवसाय मिलान → वित्तीय योजना → संबंधित योजना सुझाव → अगले व्यावहारिक कदम।",
        "market_title": "बाज़ार भाव", "market_desc": "**{location}** के लिए नमूना बाज़ार जानकारी। इसका उपयोग केवल प्रदर्शन और योजना के लिए करें; वित्तीय निर्णय से पहले वर्तमान स्थानीय मंडी भाव की पुष्टि करें।",
        "filter": "फसल श्रेणी से फ़िल्टर करें", "all": "सभी", "board": "फसल बाज़ार बोर्ड", "showing": "चयनित प्रदर्शन बाज़ार {location} के लिए {count} फसलें दिखाई जा रही हैं",
        "selected_crop": "चयनित फसल", "choose_crop": "फसल चुनें", "crop": "फसल", "sample_price": "नमूना भाव", "trend": "रुझान",
        "increasing": "बढ़ रहा है", "stable": "स्थिर", "decreasing": "घट रहा है", "market_note": "महत्वपूर्ण: स्थान कारक और भाव नियंत्रित प्रदर्शन डेटा हैं, लाइव बाज़ार डेटा नहीं।",
        "scheme_title": "सरकारी योजनाएँ", "scheme_desc": "ग्रामीण उद्यमियों, किसानों, विक्रेताओं, खाद्य प्रसंस्करण इकाइयों और कारीगरों के लिए उपयोगी योजनाएँ देखें।",
        "search": "योजनाएँ खोजें", "placeholder": "उदाहरण: भोजन, ऋण, किसान, कारीगर", "best_for": "किसके लिए", "key": "मुख्य जानकारी", "why": "यह कैसे मदद कर सकती है", "source": "आधिकारिक स्रोत",
        "scheme_warning": "योजना की पात्रता, ऋण स्वीकृति, सब्सिडी और शर्तें आधिकारिक दिशानिर्देश तथा आवेदक की स्थिति पर निर्भर करती हैं। आवेदन से पहले संबंधित सरकारी पोर्टल या बैंक से जानकारी सत्यापित करें।",
        "finance_title": "वित्तीय सहायक", "profit_tab": "📊 लाभ कैलकुलेटर", "emi_tab": "🏦 ऋण EMI कैलकुलेटर",
        "profit_est": "लाभ अनुमान", "quantity": "मात्रा", "purchase": "प्रति इकाई खरीद लागत", "selling": "प्रति इकाई बिक्री मूल्य", "other": "अन्य लागत",
        "total_cost": "कुल लागत", "revenue": "राजस्व", "profit": "अनुमानित लाभ", "positive": "इस उदाहरण में अनुमानित लाभ सकारात्मक है।",
        "break_even": "यह उदाहरण लगभग ब्रेक-ईवन पर है।", "loss": "इस उदाहरण में अनुमानित नुकसान है। मूल्य और लागत की समीक्षा करें।",
        "loan": "ऋण राशि", "rate": "वार्षिक ब्याज दर (%)", "period": "ऋण अवधि (वर्ष)", "monthly": "मासिक EMI", "total_payment": "कुल भुगतान", "interest": "कुल ब्याज",
        "loan_note": "वास्तविक ऋण शर्तें, ब्याज दर, शुल्क और स्वीकृति ऋणदाता पर निर्भर करते हैं।",
        "business_title": "व्यवसाय सुझाव", "business_desc": "अपनी स्थिति के बारे में ग्राम सहायक को बताएं। प्रोटोटाइप पूंजी, संसाधन, रुचि, पानी, अनुभव और स्थान के आधार पर व्यवसायों का स्कोर करेगा।",
        "capital": "💰 उपलब्ध पूंजी (₹)", "resource": "🧰 मुख्य उपलब्ध संसाधन", "interest_input": "❤️ मुख्य व्यवसाय रुचि", "water": "💧 पानी की उपलब्धता",
        "experience": "🎯 आपका अनुभव", "good": "अच्छी", "limited": "सीमित", "not_applicable": "लागू नहीं", "not_sure": "पता नहीं",
        "beginner": "शुरुआती", "some": "कुछ अनुभव", "experienced": "अनुभवी", "location_note": "📍 चुने गए बाज़ार के अनुसार सुझाव बदला जाएगा: **{location}**",
        "generate": "🔍 व्यवसाय सुझाव बनाएं", "three": "आपकी जानकारी के आधार पर तीन सबसे मजबूत प्रोटोटाइप सुझाव ये हैं।", "match": "मिलान",
        "investment": "अनुमानित निवेश", "model": "व्यवसाय मॉडल", "why_match": "यह क्यों उपयुक्त है", "risk": "मुख्य जोखिम", "steps": "सुझाए गए शुरुआती कदम", "relevant": "संभावित संबंधित योजनाएँ",
        "next_action": "📌 सुझाया गया अगला कदम", "below": "आपकी वर्तमान पूंजी **{business}** के सामान्य शुरुआती निवेश से कम है। छोटे पायलट, बचत, पात्र वित्तपोषण या कम पूंजी वाले व्यवसाय पर विचार करें।",
        "next": "अगला व्यावहारिक कदम **{business}** की सरल लागत सूची बनाना और निवेश से पहले अपेक्षित स्थानीय मांग से उसकी तुलना करना है।",
        "limit": "प्रोटोटाइप सीमा: यह प्रदर्शन व्यवसाय प्रोफाइल पर आधारित नियम-आधारित सिफारिश इंजन है। यह लाइव AI मॉडल नहीं है और लाभ की गारंटी नहीं देता।",
        "footer": "🌾 ग्राम सहायक • ग्रामीण सूक्ष्म उद्यम व्यवसाय मार्गदर्शन प्रोटोटाइप", "footer_note": "डेमो बाज़ार डेटा • नियम-आधारित सुझाव • निर्णय से पहले आधिकारिक योजना जानकारी सत्यापित करें",
    },
    "Kannada": {
        "language": "ಭಾಷೆ", "location": "ಮಾರುಕಟ್ಟೆ ಸ್ಥಳ", "navigate": "ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ",
        "home": "ಮುಖಪುಟ", "market": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು", "schemes": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು", "finance": "ಹಣಕಾಸು ಸಹಾಯಕ", "business": "ವ್ಯವಹಾರ ಶಿಫಾರಸು",
        "welcome": "ಗ್ರಾಮ ಸಹಾಯಕಕ್ಕೆ ಸ್ವಾಗತ", "subtitle": "ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮಿಗಳಿಗೆ ವ್ಯವಹಾರ ಮತ್ತು ಹಣಕಾಸು ಮಾರ್ಗದರ್ಶನ",
        "home_desc": "ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮಿಗಳಿಗೆ ಸ್ಥಳೀಯ ವ್ಯವಹಾರ ಅವಕಾಶಗಳನ್ನು ತಿಳಿದುಕೊಳ್ಳಲು, ಮಾದರಿ ಮಾರುಕಟ್ಟೆ ಪರಿಸ್ಥಿತಿಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು, ಹಣಕಾಸು ಅಂದಾಜು ಮಾಡಲು ಮತ್ತು ಸಂಬಂಧಿತ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಲು ಸಹಾಯ ಮಾಡುವ ಡಿಜಿಟಲ್ ಸಹಾಯಕ.",
        "crops": "ಒಳಗೊಂಡ ಬೆಳೆಗಳು", "locations": "ಸ್ಥಳಗಳು", "schemes_count": "ಯೋಜನೆಗಳು", "business_models": "ವ್ಯವಹಾರ ಮಾದರಿಗಳು",
        "selected_market": "ಆಯ್ಕೆ ಮಾಡಿದ ಮಾರುಕಟ್ಟೆ", "demo_market": "ಪ್ರಸ್ತುತ ಪ್ರದರ್ಶನ ಮಾರುಕಟ್ಟೆ", "market_disclaimer": "ಈ ಪ್ರೋಟೋಟೈಪ್‌ನಲ್ಲಿರುವ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು ಮಾದರಿ ಡೇಟಾ ಮಾತ್ರ; ಇವು ಲೈವ್ ಮಂಡಿ/API ಬೆಲೆಗಳಲ್ಲ.",
        "what_can": "ನೀವು ಏನು ಮಾಡಬಹುದು", "explore": "ಮಾರುಕಟ್ಟೆಗಳನ್ನು ನೋಡಿ", "explore_desc": "ವಿವಿಧ ಬೆಳೆಗಳು ಮತ್ತು ಸ್ಥಳಗಳ ಮಾದರಿ ಬೆಲೆಗಳನ್ನು ಹೋಲಿಸಿ.",
        "plan": "ಹಣಕಾಸು ಯೋಜಿಸಿ", "plan_desc": "ನಿರ್ಧಾರಕ್ಕೂ ಮೊದಲು ಲಾಭ, ಆದಾಯ, ವೆಚ್ಚ ಮತ್ತು ಸಾಲದ EMI ಅಂದಾಜಿಸಿ.",
        "find": "ವ್ಯವಹಾರ ಹುಡುಕಿ", "find_desc": "ಬಂಡವಾಳ, ಸಂಪನ್ಮೂಲ, ಆಸಕ್ತಿ ಮತ್ತು ಸ್ಥಳದ ಆಧಾರದ ಮೇಲೆ ವ್ಯವಹಾರಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯಿರಿ.",
        "how": "ಗ್ರಾಮ ಸಹಾಯಕ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ", "how_desc": "ನಿಮ್ಮ ಮಾಹಿತಿ → ಸ್ಥಳೀಯ ಸಂದರ್ಭ → ನಿಯಮಾಧಾರಿತ ವ್ಯವಹಾರ ಹೊಂದಾಣಿಕೆ → ಹಣಕಾಸು ಯೋಜನೆ → ಸಂಬಂಧಿತ ಯೋಜನೆ ಸಲಹೆಗಳು → ಮುಂದಿನ ಪ್ರಾಯೋಗಿಕ ಹಂತಗಳು.",
        "market_title": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು", "market_desc": "**{location}** ಗಾಗಿ ಮಾದರಿ ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ. ಇದನ್ನು ಪ್ರದರ್ಶನ ಮತ್ತು ಯೋಜನೆಗಾಗಿ ಮಾತ್ರ ಬಳಸಿ; ಹಣಕಾಸು ನಿರ್ಧಾರಕ್ಕೂ ಮೊದಲು ಪ್ರಸ್ತುತ ಸ್ಥಳೀಯ ಮಂಡಿ ಬೆಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "filter": "ಬೆಳೆ ವರ್ಗದ ಮೂಲಕ ಫಿಲ್ಟರ್ ಮಾಡಿ", "all": "ಎಲ್ಲಾ", "board": "ಬೆಳೆ ಮಾರುಕಟ್ಟೆ ಫಲಕ", "showing": "ಆಯ್ಕೆ ಮಾಡಿದ ಪ್ರದರ್ಶನ ಮಾರುಕಟ್ಟೆ {location} ಗಾಗಿ {count} ಬೆಳೆಗಳನ್ನು ತೋರಿಸಲಾಗುತ್ತಿದೆ",
        "selected_crop": "ಆಯ್ಕೆ ಮಾಡಿದ ಬೆಳೆ", "choose_crop": "ಬೆಳೆ ಆಯ್ಕೆ ಮಾಡಿ", "crop": "ಬೆಳೆ", "sample_price": "ಮಾದರಿ ಬೆಲೆ", "trend": "ಪ್ರವೃತ್ತಿ",
        "increasing": "ಏರಿಕೆ", "stable": "ಸ್ಥಿರ", "decreasing": "ಇಳಿಕೆ", "market_note": "ಮುಖ್ಯ: ಸ್ಥಳದ ಅಂಶಗಳು ಮತ್ತು ಬೆಲೆಗಳು ನಿಯಂತ್ರಿತ ಪ್ರದರ್ಶನ ಡೇಟಾ; ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಫೀಡ್ ಅಲ್ಲ.",
        "scheme_title": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು", "scheme_desc": "ಗ್ರಾಮೀಣ ಉದ್ಯಮಿಗಳು, ರೈತರು, ಮಾರಾಟಗಾರರು, ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕಗಳು ಮತ್ತು ಕರಕುಶಲಗಾರರಿಗೆ ಸಂಬಂಧಿಸಿದ ಯೋಜನೆಗಳನ್ನು ನೋಡಿ.",
        "search": "ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ", "placeholder": "ಉದಾಹರಣೆ: ಆಹಾರ, ಸಾಲ, ರೈತ, ಕರಕುಶಲಗಾರ", "best_for": "ಯಾರಿಗೆ ಸೂಕ್ತ", "key": "ಮುಖ್ಯ ಮಾಹಿತಿ", "why": "ಇದು ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು", "source": "ಅಧಿಕೃತ ಮೂಲ",
        "scheme_warning": "ಯೋಜನೆಯ ಅರ್ಹತೆ, ಸಾಲ ಅನುಮೋದನೆ, ಸಬ್ಸಿಡಿ ಮತ್ತು ಷರತ್ತುಗಳು ಅಧಿಕೃತ ಮಾರ್ಗಸೂಚಿಗಳು ಮತ್ತು ಅರ್ಜಿದಾರರ ಪರಿಸ್ಥಿತಿಯ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ. ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು ಸಂಬಂಧಿತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್ ಅಥವಾ ಬ್ಯಾಂಕ್ ಮೂಲಕ ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "finance_title": "ಹಣಕಾಸು ಸಹಾಯಕ", "profit_tab": "📊 ಲಾಭ ಕ್ಯಾಲ್ಕುಲೇಟರ್", "emi_tab": "🏦 ಸಾಲ EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "profit_est": "ಲಾಭ ಅಂದಾಜು", "quantity": "ಪ್ರಮಾಣ", "purchase": "ಪ್ರತಿ ಘಟಕ ಖರೀದಿ ವೆಚ್ಚ", "selling": "ಪ್ರತಿ ಘಟಕ ಮಾರಾಟ ಬೆಲೆ", "other": "ಇತರೆ ವೆಚ್ಚಗಳು",
        "total_cost": "ಒಟ್ಟು ವೆಚ್ಚ", "revenue": "ಆದಾಯ", "profit": "ಅಂದಾಜು ಲಾಭ", "positive": "ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಅಂದಾಜು ಲಾಭ ಧನಾತ್ಮಕವಾಗಿದೆ.",
        "break_even": "ಈ ಉದಾಹರಣೆ ಸುಮಾರು ಬ್ರೇಕ್-ಈವನ್ ಸ್ಥಿತಿಯಲ್ಲಿದೆ.", "loss": "ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಅಂದಾಜು ನಷ್ಟವಿದೆ. ಬೆಲೆ ಮತ್ತು ವೆಚ್ಚಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "loan": "ಸಾಲದ ಮೊತ್ತ", "rate": "ವಾರ್ಷಿಕ ಬಡ್ಡಿ ದರ (%)", "period": "ಸಾಲದ ಅವಧಿ (ವರ್ಷಗಳು)", "monthly": "ಮಾಸಿಕ EMI", "total_payment": "ಒಟ್ಟು ಪಾವತಿ", "interest": "ಒಟ್ಟು ಬಡ್ಡಿ",
        "loan_note": "ನಿಜವಾದ ಸಾಲದ ಷರತ್ತುಗಳು, ಬಡ್ಡಿದರ, ಶುಲ್ಕಗಳು ಮತ್ತು ಅನುಮೋದನೆ ಸಾಲದಾತರ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
        "business_title": "ವ್ಯವಹಾರ ಶಿಫಾರಸು", "business_desc": "ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಯನ್ನು ಗ್ರಾಮ ಸಹಾಯಕಕ್ಕೆ ತಿಳಿಸಿ. ಪ್ರೋಟೋಟೈಪ್ ಬಂಡವಾಳ, ಸಂಪನ್ಮೂಲ, ಆಸಕ್ತಿ, ನೀರಿನ ಲಭ್ಯತೆ, ಅನುಭವ ಮತ್ತು ಸ್ಥಳದ ಆಧಾರದ ಮೇಲೆ ವ್ಯವಹಾರಗಳಿಗೆ ಅಂಕ ನೀಡುತ್ತದೆ.",
        "capital": "💰 ಲಭ್ಯವಿರುವ ಬಂಡವಾಳ (₹)", "resource": "🧰 ಮುಖ್ಯ ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲ", "interest_input": "❤️ ಮುಖ್ಯ ವ್ಯವಹಾರ ಆಸಕ್ತಿ", "water": "💧 ನೀರಿನ ಲಭ್ಯತೆ",
        "experience": "🎯 ನಿಮ್ಮ ಅನುಭವ", "good": "ಉತ್ತಮ", "limited": "ಸೀಮಿತ", "not_applicable": "ಅನ್ವಯಿಸುವುದಿಲ್ಲ", "not_sure": "ಖಚಿತವಿಲ್ಲ",
        "beginner": "ಆರಂಭಿಕ", "some": "ಸ್ವಲ್ಪ ಅನುಭವ", "experienced": "ಅನುಭವ ಹೊಂದಿರುವವರು", "location_note": "📍 ಆಯ್ಕೆ ಮಾಡಿದ ಮಾರುಕಟ್ಟೆಗೆ ಅನುಗುಣವಾಗಿ ಶಿಫಾರಸು ಬದಲಾಗುತ್ತದೆ: **{location}**",
        "generate": "🔍 ವ್ಯವಹಾರ ಶಿಫಾರಸುಗಳನ್ನು ರಚಿಸಿ", "three": "ನಿಮ್ಮ ಮಾಹಿತಿಗೆ ಹೊಂದುವ ಮೂರು ಉತ್ತಮ ಪ್ರೋಟೋಟೈಪ್ ಶಿಫಾರಸುಗಳು ಇಲ್ಲಿವೆ.", "match": "ಹೊಂದಾಣಿಕೆ",
        "investment": "ಅಂದಾಜು ಹೂಡಿಕೆ", "model": "ವ್ಯವಹಾರ ಮಾದರಿ", "why_match": "ಇದು ಏಕೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ", "risk": "ಮುಖ್ಯ ಅಪಾಯ", "steps": "ಸೂಚಿಸಿದ ಆರಂಭಿಕ ಹಂತಗಳು", "relevant": "ಸಂಬಂಧಿತವಾಗಿರಬಹುದಾದ ಯೋಜನೆಗಳು",
        "next_action": "📌 ಸೂಚಿಸಿದ ಮುಂದಿನ ಕ್ರಮ", "below": "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಬಂಡವಾಳವು **{business}** ಗೆ ಸಾಮಾನ್ಯ ಆರಂಭಿಕ ಹೂಡಿಕೆಗಿಂತ ಕಡಿಮೆಯಾಗಿದೆ. ಸಣ್ಣ ಪೈಲಟ್, ಉಳಿತಾಯ, ಅರ್ಹ ಹಣಕಾಸು ಅಥವಾ ಕಡಿಮೆ ಬಂಡವಾಳದ ವ್ಯವಹಾರವನ್ನು ಪರಿಗಣಿಸಿ.",
        "next": "ಮುಂದಿನ ಪ್ರಾಯೋಗಿಕ ಹಂತವೆಂದರೆ **{business}** ಗಾಗಿ ಸರಳ ವೆಚ್ಚಪಟ್ಟಿ ತಯಾರಿಸಿ, ಹೂಡಿಕೆ ಮಾಡುವ ಮೊದಲು ನಿರೀಕ್ಷಿತ ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯೊಂದಿಗೆ ಹೋಲಿಸುವುದು.",
        "limit": "ಪ್ರೋಟೋಟೈಪ್ ಮಿತಿ: ಇದು ಪ್ರದರ್ಶನ ವ್ಯವಹಾರ ಪ್ರೊಫೈಲ್‌ಗಳನ್ನು ಬಳಸುವ ನಿಯಮಾಧಾರಿತ ಶಿಫಾರಸು ಎಂಜಿನ್. ಇದು ಲೈವ್ AI ಮಾದರಿ ಅಲ್ಲ ಮತ್ತು ಲಾಭದ ಖಾತರಿ ನೀಡುವುದಿಲ್ಲ.",
        "footer": "🌾 ಗ್ರಾಮ ಸಹಾಯಕ • ಗ್ರಾಮೀಣ ಸಣ್ಣ ಉದ್ಯಮ ವ್ಯವಹಾರ ಮಾರ್ಗದರ್ಶನ ಪ್ರೋಟೋಟೈಪ್", "footer_note": "ಡೆಮೊ ಮಾರುಕಟ್ಟೆ ಡೇಟಾ • ನಿಯಮಾಧಾರಿತ ಶಿಫಾರಸುಗಳು • ನಿರ್ಧಾರಕ್ಕೂ ಮೊದಲು ಅಧಿಕೃತ ಯೋಜನೆ ಮಾಹಿತಿಯನ್ನು ಪರಿಶೀಲಿಸಿ",
    }
}

# Display translations for the crop/category/trend content.
DATA_TR = {
    "Hindi": {
        "Increasing":"बढ़ रहा है","Stable":"स्थिर","Decreasing":"घट रहा है",
        "Vegetable":"सब्ज़ी","Leafy":"पत्तेदार","Cereal":"अनाज","Oilseed":"तिलहन","Pulse":"दलहन","Commercial":"व्यावसायिक","Spice":"मसाला","Horticulture":"बागवानी","Fruit":"फल",
        "Tomato":"टमाटर","Onion":"प्याज़","Potato":"आलू","Carrot":"गाजर","Beans":"बीन्स","Brinjal":"बैंगन","Cabbage":"पत्तागोभी","Cauliflower":"फूलगोभी","Capsicum":"शिमला मिर्च","Green Chilli":"हरी मिर्च","Lady Finger":"भिंडी","Bottle Gourd":"लौकी","Bitter Gourd":"करेला","Cucumber":"खीरा","Pumpkin":"कद्दू","Drumstick":"सहजन","Peas":"मटर","Beetroot":"चुकंदर","Radish":"मूली","Spinach":"पालक","Coriander":"धनिया","Fenugreek Leaves":"मेथी","Maize":"मक्का","Wheat":"गेहूँ","Rice":"चावल","Ragi":"रागी","Jowar":"ज्वार","Bajra":"बाजरा","Groundnut":"मूंगफली","Sunflower":"सूरजमुखी","Soybean":"सोयाबीन","Tur":"तूर दाल","Green Gram":"मूंग","Black Gram":"उड़द","Bengal Gram":"चना","Cotton":"कपास","Sugarcane":"गन्ना","Turmeric":"हल्दी","Chilli":"मिर्च","Ginger":"अदरक","Garlic":"लहसुन","Coconut":"नारियल","Banana":"केला","Mango":"आम","Papaya":"पपीता","Guava":"अमरूद"
    },
    "Kannada": {
        "Increasing":"ಏರಿಕೆ","Stable":"ಸ್ಥಿರ","Decreasing":"ಇಳಿಕೆ",
        "Vegetable":"ತರಕಾರಿ","Leafy":"ಸೊಪ್ಪು","Cereal":"ಧಾನ್ಯ","Oilseed":"ಎಣ್ಣೆಬೀಜ","Pulse":"ಬೇಳೆ","Commercial":"ವಾಣಿಜ್ಯ","Spice":"ಮಸಾಲೆ","Horticulture":"ತೋಟಗಾರಿಕೆ","Fruit":"ಹಣ್ಣು",
        "Tomato":"ಟೊಮ್ಯಾಟೊ","Onion":"ಈರುಳ್ಳಿ","Potato":"ಆಲೂಗಡ್ಡೆ","Carrot":"ಕ್ಯಾರೆಟ್","Beans":"ಬೀನ್ಸ್","Brinjal":"ಬದನೆಕಾಯಿ","Cabbage":"ಎಲೆಕೋಸು","Cauliflower":"ಹೂಕೋಸು","Capsicum":"ಕ್ಯಾಪ್ಸಿಕಂ","Green Chilli":"ಹಸಿರು ಮೆಣಸಿನಕಾಯಿ","Lady Finger":"ಬೆಂಡೆಕಾಯಿ","Bottle Gourd":"ಸೋರೆಕಾಯಿ","Bitter Gourd":"ಹಾಗಲಕಾಯಿ","Cucumber":"ಸೌತೆಕಾಯಿ","Pumpkin":"ಕುಂಬಳಕಾಯಿ","Drumstick":"ನುಗ್ಗೆಕಾಯಿ","Peas":"ಬಟಾಣಿ","Beetroot":"ಬೀಟ್ರೂಟ್","Radish":"ಮೂಲಂಗಿ","Spinach":"ಪಾಲಕ್ ಸೊಪ್ಪು","Coriander":"ಕೊತ್ತಂಬರಿ ಸೊಪ್ಪು","Fenugreek Leaves":"ಮೆಂತ್ಯ ಸೊಪ್ಪು","Maize":"ಮೆಕ್ಕೆಜೋಳ","Wheat":"ಗೋಧಿ","Rice":"ಅಕ್ಕಿ","Ragi":"ರಾಗಿ","Jowar":"ಜೋಳ","Bajra":"ಸಜ್ಜೆ","Groundnut":"ಕಡಲೆಕಾಯಿ","Sunflower":"ಸೂರ್ಯಕಾಂತಿ","Soybean":"ಸೋಯಾಬೀನ್","Tur":"ತೊಗರಿ","Green Gram":"ಹೆಸರುಕಾಳು","Black Gram":"ಉದ್ದು","Bengal Gram":"ಕಡಲೆ","Cotton":"ಹತ್ತಿ","Sugarcane":"ಕಬ್ಬು","Turmeric":"ಅರಿಶಿನ","Chilli":"ಮೆಣಸಿನಕಾಯಿ","Ginger":"ಶುಂಠಿ","Garlic":"ಬೆಳ್ಳುಳ್ಳಿ","Coconut":"ತೆಂಗಿನಕಾಯಿ","Banana":"ಬಾಳೆಹಣ್ಣು","Mango":"ಮಾವು","Papaya":"ಪಪ್ಪಾಯಿ","Guava":"ಸೀಬೆಹಣ್ಣು"
    }
}

def tr_data(value):
    return DATA_TR.get(language, {}).get(value, value)

def tr(key, **kwargs):
    value = TEXT[language].get(key, TEXT["English"].get(key, key))
    return value.format(**kwargs) if kwargs else value

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("## 🌾 Gram Sahayak")
    st.divider()

    LANGUAGE_NAMES = {
        "English": "English",
        "Hindi": "हिंदी",
        "Kannada": "ಕನ್ನಡ"
    }

    language = st.selectbox(
        "🌐",
        ["English", "Hindi", "Kannada"],
        format_func=lambda x: LANGUAGE_NAMES[x]
    )

    locations = [
        "Hubballi", "Dharwad", "Belagavi", "Bengaluru", "Mysuru", "Shivamogga",
        "Davanagere", "Gadag", "Haveri", "Vijayapura", "Kalaburagi", "Raichur",
        "Tumakuru", "Chitradurga"
    ]

    location = st.selectbox("📍 " + tr("location"), locations)

    st.divider()

    page_values = ["Home", "Market Prices", "Government Schemes", "Financial Assistant", "Business Recommendation"]
    page_labels = {
        "Home": "🏠 " + tr("home"),
        "Market Prices": "📈 " + tr("market"),
        "Government Schemes": "🏛️ " + tr("schemes"),
        "Financial Assistant": "💰 " + tr("finance"),
        "Business Recommendation": "💡 " + tr("business")
    }

    page = st.radio(
        tr("navigate"),
        page_values,
        format_func=lambda x: page_labels[x]
    )

T = TEXT[language]
# ============================================================
# MARKET DATA
# ============================================================

# Demo/sample prices. These are NOT live mandi/API prices.
CROP_DATA = {
    "Tomato": {"price": 30, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Onion": {"price": 35, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Potato": {"price": 28, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Carrot": {"price": 40, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Beans": {"price": 55, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},

    # 30+ additional crops
    "Brinjal": {"price": 32, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Cabbage": {"price": 24, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Cauliflower": {"price": 38, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Capsicum": {"price": 62, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Green Chilli": {"price": 58, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Lady Finger": {"price": 45, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Bottle Gourd": {"price": 30, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Bitter Gourd": {"price": 48, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Cucumber": {"price": 30, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Pumpkin": {"price": 22, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Drumstick": {"price": 70, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Peas": {"price": 65, "unit": "kg", "trend": "Increasing", "category": "Vegetable"},
    "Beetroot": {"price": 36, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Radish": {"price": 26, "unit": "kg", "trend": "Stable", "category": "Vegetable"},
    "Spinach": {"price": 25, "unit": "kg", "trend": "Increasing", "category": "Leafy"},
    "Coriander": {"price": 55, "unit": "kg", "trend": "Increasing", "category": "Leafy"},
    "Fenugreek Leaves": {"price": 48, "unit": "kg", "trend": "Stable", "category": "Leafy"},

    "Maize": {"price": 24, "unit": "kg", "trend": "Stable", "category": "Cereal"},
    "Wheat": {"price": 30, "unit": "kg", "trend": "Stable", "category": "Cereal"},
    "Rice": {"price": 42, "unit": "kg", "trend": "Stable", "category": "Cereal"},
    "Ragi": {"price": 38, "unit": "kg", "trend": "Increasing", "category": "Cereal"},
    "Jowar": {"price": 34, "unit": "kg", "trend": "Increasing", "category": "Cereal"},
    "Bajra": {"price": 32, "unit": "kg", "trend": "Stable", "category": "Cereal"},

    "Groundnut": {"price": 75, "unit": "kg", "trend": "Increasing", "category": "Oilseed"},
    "Sunflower": {"price": 58, "unit": "kg", "trend": "Stable", "category": "Oilseed"},
    "Soybean": {"price": 48, "unit": "kg", "trend": "Stable", "category": "Oilseed"},
    "Tur": {"price": 105, "unit": "kg", "trend": "Increasing", "category": "Pulse"},
    "Green Gram": {"price": 92, "unit": "kg", "trend": "Stable", "category": "Pulse"},
    "Black Gram": {"price": 88, "unit": "kg", "trend": "Stable", "category": "Pulse"},
    "Bengal Gram": {"price": 70, "unit": "kg", "trend": "Stable", "category": "Pulse"},

    "Cotton": {"price": 72, "unit": "kg", "trend": "Increasing", "category": "Commercial"},
    "Sugarcane": {"price": 3.6, "unit": "kg", "trend": "Stable", "category": "Commercial"},
    "Turmeric": {"price": 145, "unit": "kg", "trend": "Increasing", "category": "Spice"},
    "Chilli": {"price": 190, "unit": "kg", "trend": "Increasing", "category": "Spice"},
    "Ginger": {"price": 105, "unit": "kg", "trend": "Increasing", "category": "Spice"},
    "Garlic": {"price": 120, "unit": "kg", "trend": "Stable", "category": "Spice"},
    "Coconut": {"price": 38, "unit": "piece", "trend": "Stable", "category": "Horticulture"},
    "Banana": {"price": 42, "unit": "kg", "trend": "Stable", "category": "Fruit"},
    "Mango": {"price": 65, "unit": "kg", "trend": "Increasing", "category": "Fruit"},
    "Papaya": {"price": 38, "unit": "kg", "trend": "Stable", "category": "Fruit"},
    "Guava": {"price": 55, "unit": "kg", "trend": "Increasing", "category": "Fruit"},
}

# Location multiplier = demonstration of location-sensitive pricing.
# It is intentionally labelled as sample data, not live mandi data.
LOCATION_FACTOR = {
    "Hubballi": 1.00,
    "Dharwad": 0.98,
    "Belagavi": 1.03,
    "Bengaluru": 1.18,
    "Mysuru": 1.08,
    "Shivamogga": 1.02,
    "Davanagere": 0.97,
    "Gadag": 0.95,
    "Haveri": 0.96,
    "Vijayapura": 0.94,
    "Kalaburagi": 0.96,
    "Raichur": 0.95,
    "Tumakuru": 1.05,
    "Chitradurga": 0.96,
}

# ============================================================
# BUSINESS PROFILES
# ============================================================

BUSINESSES = [
    {
        "name": "Vegetable Cultivation",
        "capital": (25000, 250000),
        "resources": ["Land", "Water", "Agricultural tools"],
        "interests": ["Farming", "Agriculture", "Vegetables"],
        "locations": ["Hubballi", "Dharwad", "Belagavi", "Shivamogga", "Haveri",
                      "Davanagere", "Gadag", "Vijayapura", "Kalaburagi", "Raichur", "Tumakuru"],
        "investment": "₹25,000 – ₹2.5 lakh",
        "model": "Grow vegetables → sell to local markets, retailers, hotels or direct customers.",
        "risk": "Weather, water availability and price fluctuations.",
        "steps": [
            "Select crops based on local demand and water availability.",
            "Estimate seed, labour, irrigation and transport costs.",
            "Plan more than one sales channel instead of depending on a single buyer."
        ],
        "schemes": ["Kisan Credit Card", "PMEGP", "Agriculture Infrastructure Fund"]
    },
    {
        "name": "Small Food Processing Unit",
        "capital": (75000, 1000000),
        "resources": ["Kitchen/Workspace", "Food processing equipment", "Raw materials"],
        "interests": ["Food", "Cooking", "Processing", "Snacks"],
        "locations": locations,
        "investment": "₹75,000 – ₹10 lakh+",
        "model": "Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.",
        "risk": "Food safety, packaging, shelf life and market access.",
        "steps": [
            "Choose one product with a clear local customer segment.",
            "Calculate raw material, packaging, labour and selling costs.",
            "Test a small batch before investing in larger equipment."
        ],
        "schemes": ["PMFME", "MUDRA", "PMEGP"]
    },
    {
        "name": "Grocery & Daily-Needs Store",
        "capital": (100000, 700000),
        "resources": ["Shop space", "Working capital", "Supplier network"],
        "interests": ["Retail", "Shopping", "Customer service", "Trading"],
        "locations": locations,
        "investment": "₹1 lakh – ₹7 lakh",
        "model": "Sell essential household products with repeat local demand.",
        "risk": "Competition, inventory management and credit sales.",
        "steps": [
            "Start with fast-moving essentials instead of excessive inventory.",
            "Track daily sales and stock movement.",
            "Add high-demand local products after observing customer behaviour."
        ],
        "schemes": ["MUDRA", "PMEGP"]
    },
    {
        "name": "Street Food / Snack Business",
        "capital": (30000, 300000),
        "resources": ["Kitchen equipment", "Small stall/shop", "Food preparation skills"],
        "interests": ["Food", "Cooking", "Customer service"],
        "locations": locations,
        "investment": "₹30,000 – ₹3 lakh",
        "model": "Sell affordable snacks or meals at a high-footfall local location.",
        "risk": "Location dependency, hygiene and daily demand variation.",
        "steps": [
            "Choose a small menu with good margins.",
            "Test demand at different times of the day.",
            "Maintain hygiene, consistent quality and simple bookkeeping."
        ],
        "schemes": ["PM SVANidhi", "MUDRA", "PMEGP"]
    },
    {
        "name": "Dairy / Milk-Based Business",
        "capital": (100000, 800000),
        "resources": ["Cattle", "Fodder", "Water", "Shelter"],
        "interests": ["Dairy", "Livestock", "Agriculture"],
        "locations": locations,
        "investment": "₹1 lakh – ₹8 lakh",
        "model": "Milk production with possible value addition such as curd, paneer or ghee.",
        "risk": "Animal health, feed costs and milk-price changes.",
        "steps": [
            "Estimate feed and veterinary costs before buying animals.",
            "Identify a reliable local milk buyer.",
            "Maintain records of milk yield and animal health."
        ],
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"]
    },
    {
        "name": "Goat / Sheep Rearing",
        "capital": (60000, 500000),
        "resources": ["Land", "Shelter", "Livestock care"],
        "interests": ["Livestock", "Farming", "Animal husbandry"],
        "locations": locations,
        "investment": "₹60,000 – ₹5 lakh",
        "model": "Rear animals for meat, breeding or local livestock markets.",
        "risk": "Disease, feed costs and market-price fluctuations.",
        "steps": [
            "Start with a manageable herd size.",
            "Plan vaccination and veterinary care.",
            "Build a buyer network before scaling."
        ],
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"]
    },
    {
        "name": "Poultry Farming",
        "capital": (80000, 600000),
        "resources": ["Shelter", "Water", "Poultry equipment"],
        "interests": ["Poultry", "Livestock", "Farming"],
        "locations": locations,
        "investment": "₹80,000 – ₹6 lakh",
        "model": "Egg or broiler production for nearby markets.",
        "risk": "Feed costs, disease and price volatility.",
        "steps": [
            "Choose egg or meat production based on local demand.",
            "Calculate feed cost per bird.",
            "Maintain biosecurity and veterinary schedules."
        ],
        "schemes": ["MUDRA", "Kisan Credit Card", "PMEGP"]
    },
    {
        "name": "Local Delivery & Transport Service",
        "capital": (75000, 600000),
        "resources": ["Two-wheeler/vehicle", "Mobile phone", "Driving skills"],
        "interests": ["Transport", "Delivery", "Customer service"],
        "locations": locations,
        "investment": "₹75,000 – ₹6 lakh",
        "model": "Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.",
        "risk": "Fuel costs, vehicle maintenance and route density.",
        "steps": [
            "Map villages and shops that need regular delivery.",
            "Start with a defined service radius.",
            "Use simple digital records for orders, fuel and collections."
        ],
        "schemes": ["MUDRA", "PMEGP"]
    },
    {
        "name": "Tailoring & Garment Service",
        "capital": (30000, 250000),
        "resources": ["Sewing machine", "Workspace", "Tailoring skills"],
        "interests": ["Tailoring", "Fashion", "Handicrafts"],
        "locations": locations,
        "investment": "₹30,000 – ₹2.5 lakh",
        "model": "Alterations, stitching, school uniforms, traditional clothing and small-batch garments.",
        "risk": "Competition and seasonal demand.",
        "steps": [
            "Start with alterations and high-demand local garments.",
            "Build repeat customers through reliable delivery.",
            "Add machines only when order volume justifies them."
        ],
        "schemes": ["PM Vishwakarma", "MUDRA", "PMEGP"]
    },
    {
        "name": "Handicrafts & Local Products",
        "capital": (25000, 300000),
        "resources": ["Craft skills", "Raw materials", "Workspace"],
        "interests": ["Handicrafts", "Art", "Crafts"],
        "locations": locations,
        "investment": "₹25,000 – ₹3 lakh",
        "model": "Make baskets, decor, traditional products or locally distinctive handmade goods.",
        "risk": "Demand discovery and inconsistent order volume.",
        "steps": [
            "Identify one product with a clear customer segment.",
            "Create a small catalogue and sample products.",
            "Explore local fairs, retailers and digital selling channels."
        ],
        "schemes": ["PM Vishwakarma", "PMEGP", "MUDRA"]
    },
    {
        "name": "Farm Input & Agri Service Centre",
        "capital": (150000, 1000000),
        "resources": ["Shop", "Agriculture knowledge", "Supplier network"],
        "interests": ["Agriculture", "Retail", "Advisory"],
        "locations": locations,
        "investment": "₹1.5 lakh – ₹10 lakh+",
        "model": "Supply seeds, tools, irrigation accessories and farm-related services.",
        "risk": "Inventory, licensing requirements and seasonal demand.",
        "steps": [
            "Identify the crops and farm needs of nearby villages.",
            "Stock fast-moving inputs first.",
            "Follow all applicable licences and quality requirements."
        ],
        "schemes": ["ACABC", "MUDRA", "PMEGP"]
    },
    {
        "name": "Small Repair & Service Centre",
        "capital": (40000, 300000),
        "resources": ["Repair tools", "Workspace", "Technical skill"],
        "interests": ["Repair", "Technology", "Machines", "Electronics"],
        "locations": locations,
        "investment": "₹40,000 – ₹3 lakh",
        "model": "Repair phones, appliances, agricultural equipment or other locally needed items.",
        "risk": "Skill dependency and availability of spare parts.",
        "steps": [
            "Choose one repair category based on local demand.",
            "Keep commonly required spare parts.",
            "Build trust through transparent pricing and service records."
        ],
        "schemes": ["MUDRA", "PMEGP"]
    },
]

# ============================================================
# GOVERNMENT SCHEMES
# ============================================================

SCHEMES = [
    {
        "name": "PMEGP – Prime Minister's Employment Generation Programme",
        "best_for": "New micro-enterprises in manufacturing and eligible service/non-farm activities.",
        "description": "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.",
        "key": "For new enterprises; applicant generally must be 18+. Project and eligibility conditions apply.",
        "why": "Useful when the entrepreneur is starting a new eligible micro-enterprise and needs structured project finance.",
        "source": "KVIC / Ministry of MSME"
    },
    {
        "name": "Pradhan Mantri MUDRA Yojana (PMMY)",
        "best_for": "Small businesses needing working capital or business expansion finance.",
        "description": "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.",
        "key": "Shishu up to ₹50,000; Kishor above ₹50,000 to ₹5 lakh; Tarun above ₹5 lakh to ₹10 lakh; Tarun Plus above ₹10 lakh to ₹20 lakh for eligible repeat borrowers.",
        "why": "Useful for shops, services, food businesses, livestock-related activities and other eligible micro businesses.",
        "source": "Department of Financial Services, Ministry of Finance"
    },
    {
        "name": "PM SVANidhi",
        "best_for": "Eligible street vendors.",
        "description": "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.",
        "key": "Loan tranches can go up to ₹15,000, ₹25,000 and ₹50,000, subject to scheme conditions. Lending period has been extended to March 31, 2030.",
        "why": "Especially relevant for small street food, vending and mobile retail businesses.",
        "source": "Ministry of Housing & Urban Affairs / Government of India"
    },
    {
        "name": "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises",
        "best_for": "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.",
        "description": "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.",
        "key": "Individual micro food-processing units may receive 35% credit-linked capital subsidy up to ₹10 lakh, subject to eligibility and guidelines.",
        "why": "A strong match for spice processing, pickles, snacks, flour, local food products and value-added agricultural produce.",
        "source": "Ministry of Food Processing Industries"
    },
    {
        "name": "Kisan Credit Card (KCC)",
        "best_for": "Farmers and eligible agricultural/allied activities.",
        "description": "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.",
        "key": "Can support eligible crop and allied agricultural credit requirements through participating financial institutions.",
        "why": "Useful when the main business is farming or an eligible allied agricultural activity.",
        "source": "Government of India / Department of Financial Services"
    },
    {
        "name": "Agriculture Infrastructure Fund (AIF)",
        "best_for": "Post-harvest infrastructure and eligible community farming assets.",
        "description": "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.",
        "key": "Eligible loans can receive interest subvention of 3% per year on the loan component up to ₹2 crore, subject to scheme conditions.",
        "why": "Useful for storage, grading, primary processing and other eligible agricultural infrastructure.",
        "source": "Department of Agriculture & Farmers Welfare"
    },
    {
        "name": "Agri-Clinics and Agri-Business Centres (ACABC)",
        "best_for": "Eligible agriculture-trained entrepreneurs providing farm-related services.",
        "description": "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.",
        "key": "Eligibility, training, project cost and subsidy provisions depend on the current ACABC guidelines.",
        "why": "Useful for agriculture advisory, farm services, input-related services and other eligible agri-business models.",
        "source": "MANAGE / Ministry of Agriculture & Farmers Welfare"
    },
    {
        "name": "DAY-NRLM – Deendayal Antyodaya Yojana",
        "best_for": "Rural women-led Self Help Groups and rural livelihoods.",
        "description": "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.",
        "key": "Support is delivered through the rural livelihood mission structure and applicable state-level mechanisms.",
        "why": "Useful for group enterprises, food processing, handicrafts and other SHG-based rural businesses.",
        "source": "Ministry of Rural Development"
    },
    {
        "name": "PM Vishwakarma",
        "best_for": "Eligible traditional artisans and craftspeople.",
        "description": "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.",
        "key": "Benefits and eligible trades are subject to the official scheme guidelines.",
        "why": "Relevant to tailoring and eligible traditional craft/artisan businesses.",
        "source": "Government of India"
    },
    {
        "name": "PM-KUSUM",
        "best_for": "Eligible farmers and agricultural energy/solar applications.",
        "description": "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.",
        "key": "Component, subsidy and implementation conditions vary and are administered through the relevant authorities.",
        "why": "Relevant where reliable agricultural energy and irrigation are important to the business model.",
        "source": "Ministry of New and Renewable Energy"
    }
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def money(value):
    return f"₹{value:,.0f}"

def calculate_match(business, capital, resource, interest, water, experience, location):
    score = 0
    reasons = []

    low, high = business["capital"]

    # Capital fit
    if capital >= high:
        score += 30
        reasons.append("Your available capital comfortably covers the indicative investment range.")
    elif capital >= low:
        score += 25
        reasons.append("Your capital fits the lower-to-middle part of the indicative investment range.")
    elif capital >= low * 0.5:
        score += 12
        reasons.append("Your capital is below the typical starting range, so a smaller pilot may be needed.")
    else:
        score += 3
        reasons.append("Capital is currently limited for this model.")

    # Resource fit
    resource_lower = resource.lower()
    resource_matches = [r.lower() for r in business["resources"]]
    if any(r in resource_lower for r in resource_matches) or resource == "Not sure / I have limited resources":
        score += 20
        reasons.append("Your available resources can support this type of business.")
    else:
        score += 7
        reasons.append("You may need to arrange some additional resources before starting.")

    # Interest fit
    interest_lower = interest.lower()
    if any(x.lower() in interest_lower for x in business["interests"]):
        score += 20
        reasons.append("The business matches your stated interest.")
    else:
        score += 7

    # Water fit
    if "Water" in business["resources"] or "water" in business["name"].lower():
        if water == "Good":
            score += 10
            reasons.append("Good water availability improves feasibility.")
        elif water == "Limited":
            score += 4
            reasons.append("Limited water availability makes this business more sensitive to planning.")
        else:
            score += 1
    else:
        score += 8

    # Experience
    if experience == "Some experience":
        score += 10
        reasons.append("Your existing experience reduces the learning curve.")
    elif experience == "Experienced":
        score += 10
        reasons.append("Your experience is a strong fit for execution.")
    else:
        score += 5
        reasons.append("A small pilot and basic training are recommended before scaling.")

    # Location
    if location in business["locations"]:
        score += 10
        reasons.append(f"{location} is included in the prototype's suitable-location profile.")
    else:
        score += 5

    return min(score, 100), reasons


def scheme_for_business(business):
    return business["schemes"]



# ============================================================
# HOME
# ============================================================

if page == "Home":
    st.markdown(f"""
    <div class="hero">
        <h1>🌾 Gram Sahayak</h1>
        <p>{tr("subtitle")}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"## {tr('welcome')}")
    st.write(tr("home_desc"))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🌱 " + tr("crops"), len(CROP_DATA))
    col2.metric("📍 " + tr("locations"), len(locations))
    col3.metric("🏛️ " + tr("schemes_count"), len(SCHEMES))
    col4.metric("💡 " + tr("business_models"), len(BUSINESSES))

    st.markdown(f"### 📍 {tr('selected_market')}")
    st.info(f"{tr('demo_market')}: **{location}**. {tr('market_disclaimer')}")

    st.markdown(f"### ✨ {tr('what_can')}")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="card"><h3>📈 {tr("explore")}</h3><p>{tr("explore_desc")}</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="card"><h3>💰 {tr("plan")}</h3><p>{tr("plan_desc")}</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="card"><h3>💡 {tr("find")}</h3><p>{tr("find_desc")}</p></div>""", unsafe_allow_html=True)

    st.markdown(f"### 🔄 {tr('how')}")
    st.write(tr("how_desc"))

# ============================================================
# MARKET PRICES
# ============================================================

if page == "Market Prices":
    st.title("📈 " + tr("market_title"))
    st.write(tr("market_desc", location=location))

    categories = sorted(set(v["category"] for v in CROP_DATA.values()))
    category = st.selectbox(
        tr("filter"),
        ["All"] + categories,
        format_func=lambda x: tr("all") if x == "All" else tr_data(x)
    )

    filtered = {crop: data for crop, data in CROP_DATA.items()
                if category == "All" or data["category"] == category}

    factor = LOCATION_FACTOR.get(location, 1.0)

    st.markdown(f"### 🧺 {tr('board')}")
    st.caption(tr("showing", count=len(filtered), location=location))

    items = list(filtered.items())
    for start in range(0, len(items), 4):
        cols = st.columns(4)
        for col, (crop_name, data) in zip(cols, items[start:start + 4]):
            with col:
                adjusted = data["price"] * factor
                trend_icon = "📈" if data["trend"] == "Increasing" else ("📉" if data["trend"] == "Decreasing" else "➡️")
                st.markdown(f"""
                <div class="card">
                    <h4>🌾 {tr_data(crop_name)}</h4>
                    <p><b>{tr_data(data["category"])}</b></p>
                    <h3>₹{adjusted:,.2f} / {data["unit"]}</h3>
                    <p>{trend_icon} {tr_data(data["trend"])}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown(f"### 📊 {tr('selected_crop')}")
    crop = st.selectbox(tr("choose_crop"), list(filtered.keys()), format_func=lambda x: tr_data(x))
    selected = filtered[crop]
    sample_price = selected["price"] * factor

    a, b, c = st.columns(3)
    a.metric(tr("crop"), tr_data(crop))
    b.metric(tr("sample_price"), f"₹{sample_price:,.2f} / {selected['unit']}")
    c.metric(tr("trend"), tr_data(selected["trend"]))

    st.caption(tr("market_note"))

# ============================================================
# GOVERNMENT SCHEMES
# ============================================================

if page == "Government Schemes":
    st.title("🏛️ " + tr("scheme_title"))
    st.write(tr("scheme_desc"))

    search = st.text_input("🔎 " + tr("search"), placeholder=tr("placeholder"))

    # Search remains based on the original official English content so it is stable.
    shown = []
    for scheme in SCHEMES:
        searchable = (scheme["name"] + " " + scheme["best_for"] + " " +
                      scheme["description"] + " " + scheme["why"]).lower()
        if not search or search.lower() in searchable:
            shown.append(scheme)

    SCHEME_TR = {
        "Hindi": {
            "best": {
                "New micro-enterprises in manufacturing and eligible service/non-farm activities.":"विनिर्माण और पात्र सेवा/गैर-कृषि गतिविधियों वाले नए सूक्ष्म उद्यम।",
                "Small businesses needing working capital or business expansion finance.":"कार्यशील पूंजी या व्यवसाय विस्तार के लिए वित्त की जरूरत वाले छोटे व्यवसाय।",
                "Eligible street vendors.":"पात्र स्ट्रीट वेंडर।",
                "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.":"सूक्ष्म खाद्य-प्रसंस्करण व्यवसाय और पात्र SHG/FPO/सहकारी संस्थाएँ।",
                "Farmers and eligible agricultural/allied activities.":"किसान और पात्र कृषि/संबद्ध गतिविधियाँ।",
                "Post-harvest infrastructure and eligible community farming assets.":"फसल कटाई के बाद की अवसंरचना और पात्र सामुदायिक कृषि परिसंपत्तियाँ।",
                "Eligible agriculture-trained entrepreneurs providing farm-related services.":"पात्र कृषि-प्रशिक्षित उद्यमी जो कृषि संबंधी सेवाएँ देते हैं।",
                "Rural women-led Self Help Groups and rural livelihoods.":"ग्रामीण महिलाओं के नेतृत्व वाले स्वयं सहायता समूह और ग्रामीण आजीविका।",
                "Eligible traditional artisans and craftspeople.":"पात्र पारंपरिक कारीगर और शिल्पकार।",
                "Eligible farmers and agricultural energy/solar applications.":"पात्र किसान और कृषि ऊर्जा/सौर अनुप्रयोग।"
            },
            "desc": {
                "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.":"यह बैंक वित्त और मार्जिन-मनी सब्सिडी के माध्यम से नए सूक्ष्म उद्यमों को सहायता देने वाला क्रेडिट-लिंक्ड सरकारी कार्यक्रम है। इसका उद्देश्य विशेष रूप से ग्रामीण और नए उद्यमियों के लिए स्वरोजगार और रोजगार के अवसर बनाना है।",
                "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.":"विनिर्माण, व्यापार, सेवा और संबद्ध कृषि गतिविधियों वाले पात्र सूक्ष्म उद्यमों के लिए बिना जमानत संस्थागत ऋण उपलब्ध कराता है।",
                "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.":"स्ट्रीट वेंडरों के लिए सूक्ष्म ऋण और सहायता कार्यक्रम। पुनर्गठित योजना में क्रमिक कार्यशील पूंजी ऋण, डिजिटल अपनाने के प्रोत्साहन और व्यापक आजीविका सहायता शामिल है।",
                "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.":"सूक्ष्म खाद्य-प्रसंस्करण उद्यमों के औपचारिकीकरण, उन्नयन और क्षमता निर्माण में सहायता करता है। पात्र व्यक्तिगत इकाइयों को योजना की शर्तों के अनुसार क्रेडिट-लिंक्ड पूंजी सब्सिडी मिल सकती है।",
                "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.":"कृषि और संबद्ध कार्यशील पूंजी जरूरतों के लिए पात्रता और ऋण शर्तों के अनुसार औपचारिक ऋण सुविधा प्रदान करता है।",
                "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.":"फसल कटाई के बाद प्रबंधन और सामुदायिक कृषि परिसंपत्तियों जैसी पात्र कृषि अवसंरचना के लिए वित्तीय सहायता प्रदान करता है।",
                "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.":"प्रशिक्षित कृषि पेशेवरों/पात्र उम्मीदवारों को किसानों के लिए सलाह और कृषि सेवाएँ देने वाले एग्री-क्लिनिक और एग्री-बिजनेस केंद्र स्थापित करने में सहायता करता है।",
                "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.":"स्वयं सहायता समूहों और सामुदायिक संस्थाओं के माध्यम से वित्त, कौशल, उद्यम सहायता और टिकाऊ आजीविका तक पहुँच बेहतर करने वाला ग्रामीण आजीविका कार्यक्रम।",
                "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.":"पात्र पारंपरिक कारीगरों और शिल्पकारों को पहचान, कौशल विकास, टूलकिट, ऋण और बाजार-उन्मुख सहायता प्रदान करता है।",
                "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.":"कृषि में सौर ऊर्जा से जुड़े उपायों, पात्र सौर पंपों और योजना के अन्य घटकों को सहायता देता है।"
            }
        },
        "Kannada": {
            "best": {
                "New micro-enterprises in manufacturing and eligible service/non-farm activities.":"ಉತ್ಪಾದನೆ ಮತ್ತು ಅರ್ಹ ಸೇವೆ/ಕೃಷಿಯೇತರ ಚಟುವಟಿಕೆಗಳ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳು.",
                "Small businesses needing working capital or business expansion finance.":"ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಥವಾ ವ್ಯವಹಾರ ವಿಸ್ತರಣೆಗೆ ಹಣಕಾಸು ಬೇಕಿರುವ ಸಣ್ಣ ವ್ಯವಹಾರಗಳು.",
                "Eligible street vendors.":"ಅರ್ಹ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು.",
                "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಅರ್ಹ SHG/FPO/ಸಹಕಾರಿ ಸಂಸ್ಥೆಗಳು.",
                "Farmers and eligible agricultural/allied activities.":"ರೈತರು ಮತ್ತು ಅರ್ಹ ಕೃಷಿ/ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು.",
                "Post-harvest infrastructure and eligible community farming assets.":"ಕೊಯ್ಲಿನ ನಂತರದ ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಅರ್ಹ ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿಗಳು.",
                "Eligible agriculture-trained entrepreneurs providing farm-related services.":"ಕೃಷಿ ತರಬೇತಿ ಪಡೆದ ಅರ್ಹ ಉದ್ಯಮಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಬಂಧಿತ ಸೇವಾ ಪೂರೈಕೆದಾರರು.",
                "Rural women-led Self Help Groups and rural livelihoods.":"ಗ್ರಾಮೀಣ ಮಹಿಳೆಯರ ನೇತೃತ್ವದ ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು ಮತ್ತು ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ.",
                "Eligible traditional artisans and craftspeople.":"ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳು.",
                "Eligible farmers and agricultural energy/solar applications.":"ಅರ್ಹ ರೈತರು ಮತ್ತು ಕೃಷಿ ಶಕ್ತಿ/ಸೌರ ಅನ್ವಯಿಕೆಗಳು."
            },
            "desc": {
                "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.":"ಬ್ಯಾಂಕ್ ಹಣಕಾಸು ಮತ್ತು ಮಾರ್ಜಿನ್-ಮನಿ ಸಬ್ಸಿಡಿ ಮೂಲಕ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುವ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಸರ್ಕಾರಿ ಕಾರ್ಯಕ್ರಮ. ವಿಶೇಷವಾಗಿ ಗ್ರಾಮೀಣ ಮತ್ತು ಹೊಸ ಉದ್ಯಮಿಗಳಿಗೆ ಸ್ವಯಂ ಉದ್ಯೋಗ ಹಾಗೂ ಉದ್ಯೋಗಾವಕಾಶಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು ಇದರ ಉದ್ದೇಶ.",
                "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.":"ಉತ್ಪಾದನೆ, ವ್ಯಾಪಾರ, ಸೇವೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಗಳ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಜಾಮೀನು ಇಲ್ಲದ ಸಂಸ್ಥಾತ್ಮಕ ಸಾಲ ಒದಗಿಸುತ್ತದೆ.",
                "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.":"ಬೀದಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ಸೂಕ್ಷ್ಮ ಸಾಲ ಮತ್ತು ಬೆಂಬಲ ಕಾರ್ಯಕ್ರಮ. ಪರಿಷ್ಕೃತ ಯೋಜನೆಯಲ್ಲಿ ಹಂತ ಹಂತದ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಸಾಲ, ಡಿಜಿಟಲ್ ಬಳಕೆಗೆ ಪ್ರೋತ್ಸಾಹ ಮತ್ತು ಜೀವನೋಪಾಯ ಬೆಂಬಲ ಸೇರಿವೆ.",
                "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳ ಔಪಚಾರಿಕೀಕರಣ, ಉನ್ನತೀಕರಣ ಮತ್ತು ಸಾಮರ್ಥ್ಯ ವೃದ್ಧಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ. ಅರ್ಹ ವೈಯಕ್ತಿಕ ಘಟಕಗಳಿಗೆ ಯೋಜನೆಯ ಷರತ್ತುಗಳಂತೆ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ದೊರೆಯಬಹುದು.",
                "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.":"ಕೃಷಿ ಮತ್ತು ಸಂಬಂಧಿತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಗತ್ಯಗಳಿಗೆ ಸಾಲ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳಂತೆ ಅಧಿಕೃತ ಸಾಲ ಸೌಲಭ್ಯ ಒದಗಿಸುತ್ತದೆ.",
                "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.":"ಕೊಯ್ಲಿನ ನಂತರದ ನಿರ್ವಹಣೆ ಮತ್ತು ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿಗಳಂತಹ ಅರ್ಹ ಕೃಷಿ ಮೂಲಸೌಕರ್ಯಕ್ಕೆ ಹಣಕಾಸು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
                "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.":"ತರಬೇತಿ ಪಡೆದ ಕೃಷಿ ವೃತ್ತಿಪರರು/ಅರ್ಹ ಅಭ್ಯರ್ಥಿಗಳು ರೈತರಿಗೆ ಸಲಹೆ ಮತ್ತು ಕೃಷಿ ಸೇವೆ ನೀಡುವ ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
                "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.":"ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು ಮತ್ತು ಸಮುದಾಯ ಸಂಸ್ಥೆಗಳ ಮೂಲಕ ಹಣಕಾಸು, ಕೌಶಲ್ಯ, ಉದ್ಯಮ ಬೆಂಬಲ ಮತ್ತು ಶಾಶ್ವತ ಜೀವನೋಪಾಯಕ್ಕೆ ಪ್ರವೇಶವನ್ನು ಸುಧಾರಿಸುವ ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಕಾರ್ಯಕ್ರಮ.",
                "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.":"ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳಿಗೆ ಮಾನ್ಯತೆ, ಕೌಶಲ್ಯ ಅಭಿವೃದ್ಧಿ, ಟೂಲ್‌ಕಿಟ್, ಸಾಲ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಆಧಾರಿತ ಸಹಾಯ ನೀಡುತ್ತದೆ.",
                "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.":"ಅರ್ಹ ಸೌರ ಪಂಪ್‌ಗಳು ಮತ್ತು ಯೋಜನೆಯ ಇತರ ಘಟಕಗಳನ್ನು ಒಳಗೊಂಡಂತೆ ಕೃಷಿಯಲ್ಲಿ ಸೌರಶಕ್ತಿ ಸಂಬಂಧಿತ ಕ್ರಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ."
            }
        }
    }

    # Scheme names, key points, reasons and official-source labels.
    SCHEME_NAME_TR = {
        "Hindi": {
            "PMEGP – Prime Minister's Employment Generation Programme": "PMEGP – प्रधानमंत्री रोजगार सृजन कार्यक्रम",
            "Pradhan Mantri MUDRA Yojana (PMMY)": "प्रधानमंत्री मुद्रा योजना (PMMY)",
            "PM SVANidhi": "PM SVANidhi – प्रधानमंत्री स्ट्रीट वेंडर्स आत्मनिर्भर निधि",
            "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises": "PMFME – प्रधानमंत्री सूक्ष्म खाद्य प्रसंस्करण उद्यम औपचारिकीकरण योजना",
            "Kisan Credit Card (KCC)": "किसान क्रेडिट कार्ड (KCC)",
            "Agriculture Infrastructure Fund (AIF)": "कृषि अवसंरचना कोष (AIF)",
            "Agri-Clinics and Agri-Business Centres (ACABC)": "एग्री-क्लिनिक और एग्री-बिजनेस सेंटर (ACABC)",
            "DAY-NRLM – Deendayal Antyodaya Yojana": "DAY-NRLM – दीनदयाल अंत्योदय योजना",
            "PM Vishwakarma": "PM विश्वकर्मा",
            "PM-KUSUM": "PM-कुसुम"
        },
        "Kannada": {
            "PMEGP – Prime Minister's Employment Generation Programme": "PMEGP – ಪ್ರಧಾನ ಮಂತ್ರಿ ಉದ್ಯೋಗ ಸೃಜನ ಕಾರ್ಯಕ್ರಮ",
            "Pradhan Mantri MUDRA Yojana (PMMY)": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಮುದ್ರಾ ಯೋಜನೆ (PMMY)",
            "PM SVANidhi": "PM SVANidhi – ಪ್ರಧಾನ ಮಂತ್ರಿ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳ ಆತ್ಮನಿರ್ಭರ ನಿಧಿ",
            "PMFME – Pradhan Mantri Formalisation of Micro Food Processing Enterprises": "PMFME – ಪ್ರಧಾನ ಮಂತ್ರಿ ಸೂಕ್ಷ್ಮ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳ ಔಪಚಾರಿಕೀಕರಣ ಯೋಜನೆ",
            "Kisan Credit Card (KCC)": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC)",
            "Agriculture Infrastructure Fund (AIF)": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ (AIF)",
            "Agri-Clinics and Agri-Business Centres (ACABC)": "ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳು (ACABC)",
            "DAY-NRLM – Deendayal Antyodaya Yojana": "DAY-NRLM – ದೀನದಯಾಳ್ ಅಂತ್ಯೋದಯ ಯೋಜನೆ",
            "PM Vishwakarma": "PM ವಿಶ್ವಕರ್ಮ",
            "PM-KUSUM": "PM-ಕುಸುಮ್"
        }
    }

    SCHEME_EXTRA_TR = {
        "Hindi": {
            "key": {
                "For new enterprises; applicant generally must be 18+. Project and eligibility conditions apply.": "नए उद्यमों के लिए; आवेदक सामान्यतः 18+ होना चाहिए। परियोजना और पात्रता की शर्तें लागू होती हैं।",
                "Shishu up to ₹50,000; Kishor above ₹50,000 to ₹5 lakh; Tarun above ₹5 lakh to ₹10 lakh; Tarun Plus above ₹10 lakh to ₹20 lakh for eligible repeat borrowers.": "शिशु ₹50,000 तक; किशोर ₹50,000 से अधिक से ₹5 लाख तक; तरुण ₹5 लाख से अधिक से ₹10 लाख तक; पात्र दोबारा ऋण लेने वालों के लिए तरुण प्लस ₹10 लाख से ₹20 लाख तक।",
                "Loan tranches can go up to ₹15,000, ₹25,000 and ₹50,000, subject to scheme conditions. Lending period has been extended to March 31, 2030.": "योजना की शर्तों के अनुसार ऋण की किश्तें ₹15,000, ₹25,000 और ₹50,000 तक हो सकती हैं। ऋण अवधि 31 मार्च 2030 तक बढ़ाई गई है।",
                "Individual micro food-processing units may receive 35% credit-linked capital subsidy up to ₹10 lakh, subject to eligibility and guidelines.": "पात्रता और दिशानिर्देशों के अनुसार व्यक्तिगत सूक्ष्म खाद्य-प्रसंस्करण इकाइयों को ₹10 लाख तक 35% क्रेडिट-लिंक्ड पूंजी सब्सिडी मिल सकती है।",
                "Can support eligible crop and allied agricultural credit requirements through participating financial institutions.": "भाग लेने वाली वित्तीय संस्थाओं के माध्यम से पात्र फसल और संबद्ध कृषि ऋण आवश्यकताओं को पूरा करने में सहायता कर सकता है।",
                "Eligible loans can receive interest subvention of 3% per year on the loan component up to ₹2 crore, subject to scheme conditions.": "योजना की शर्तों के अनुसार पात्र ऋण के ₹2 करोड़ तक के ऋण घटक पर प्रति वर्ष 3% ब्याज सहायता मिल सकती है।",
                "Eligibility, training, project cost and subsidy provisions depend on the current ACABC guidelines.": "पात्रता, प्रशिक्षण, परियोजना लागत और सब्सिडी के प्रावधान वर्तमान ACABC दिशानिर्देशों पर निर्भर करते हैं।",
                "Support is delivered through the rural livelihood mission structure and applicable state-level mechanisms.": "सहायता ग्रामीण आजीविका मिशन की संरचना और लागू राज्य-स्तरीय व्यवस्थाओं के माध्यम से दी जाती है।",
                "Benefits and eligible trades are subject to the official scheme guidelines.": "लाभ और पात्र व्यवसाय आधिकारिक योजना दिशानिर्देशों के अधीन हैं।",
                "Component, subsidy and implementation conditions vary and are administered through the relevant authorities.": "घटक, सब्सिडी और कार्यान्वयन की शर्तें अलग-अलग हो सकती हैं और संबंधित प्राधिकरणों द्वारा लागू की जाती हैं।"
            },
            "why": {
                "Useful when the entrepreneur is starting a new eligible micro-enterprise and needs structured project finance.": "जब उद्यमी नया पात्र सूक्ष्म उद्यम शुरू कर रहा हो और उसे संरचित परियोजना वित्त की आवश्यकता हो, तब उपयोगी।",
                "Useful for shops, services, food businesses, livestock-related activities and other eligible micro businesses.": "दुकानों, सेवाओं, खाद्य व्यवसायों, पशुपालन संबंधी गतिविधियों और अन्य पात्र सूक्ष्म व्यवसायों के लिए उपयोगी।",
                "Especially relevant for small street food, vending and mobile retail businesses.": "छोटे स्ट्रीट फूड, वेंडिंग और मोबाइल रिटेल व्यवसायों के लिए विशेष रूप से उपयोगी।",
                "A strong match for spice processing, pickles, snacks, flour, local food products and value-added agricultural produce.": "मसाला प्रसंस्करण, अचार, स्नैक्स, आटा, स्थानीय खाद्य उत्पाद और मूल्यवर्धित कृषि उपज के लिए विशेष रूप से उपयोगी।",
                "Useful when the main business is farming or an eligible allied agricultural activity.": "जब मुख्य व्यवसाय खेती या पात्र संबद्ध कृषि गतिविधि हो, तब उपयोगी।",
                "Useful for storage, grading, primary processing and other eligible agricultural infrastructure.": "भंडारण, ग्रेडिंग, प्राथमिक प्रसंस्करण और अन्य पात्र कृषि अवसंरचना के लिए उपयोगी।",
                "Useful for agriculture advisory, farm services, input-related services and other eligible agri-business models.": "कृषि सलाह, कृषि सेवाओं, इनपुट संबंधी सेवाओं और अन्य पात्र कृषि-व्यवसाय मॉडलों के लिए उपयोगी।",
                "Useful for group enterprises, food processing, handicrafts and other SHG-based rural businesses.": "समूह उद्यमों, खाद्य प्रसंस्करण, हस्तशिल्प और अन्य SHG-आधारित ग्रामीण व्यवसायों के लिए उपयोगी।",
                "Relevant to tailoring and eligible traditional craft/artisan businesses.": "सिलाई और पात्र पारंपरिक कारीगर व्यवसायों के लिए उपयोगी।",
                "Relevant where reliable agricultural energy and irrigation are important to the business model.": "जहाँ विश्वसनीय कृषि ऊर्जा और सिंचाई व्यवसाय मॉडल के लिए महत्वपूर्ण हैं, वहाँ उपयोगी।"
            },
            "source": {
                "KVIC / Ministry of MSME": "KVIC / सूक्ष्म, लघु और मध्यम उद्यम मंत्रालय",
                "Department of Financial Services, Ministry of Finance": "वित्तीय सेवा विभाग, वित्त मंत्रालय",
                "Ministry of Housing & Urban Affairs / Government of India": "आवास और शहरी कार्य मंत्रालय / भारत सरकार",
                "Ministry of Food Processing Industries": "खाद्य प्रसंस्करण उद्योग मंत्रालय",
                "Government of India / Department of Financial Services": "भारत सरकार / वित्तीय सेवा विभाग",
                "Department of Agriculture & Farmers Welfare": "कृषि एवं किसान कल्याण विभाग",
                "MANAGE / Ministry of Agriculture & Farmers Welfare": "MANAGE / कृषि एवं किसान कल्याण मंत्रालय",
                "Ministry of Rural Development": "ग्रामीण विकास मंत्रालय",
                "Government of India": "भारत सरकार",
                "Ministry of New and Renewable Energy": "नवीन और नवीकरणीय ऊर्जा मंत्रालय"
            }
        },
        "Kannada": {
            "key": {
                "For new enterprises; applicant generally must be 18+. Project and eligibility conditions apply.": "ಹೊಸ ಉದ್ಯಮಗಳಿಗೆ; ಅರ್ಜಿದಾರರು ಸಾಮಾನ್ಯವಾಗಿ 18+ ಆಗಿರಬೇಕು. ಯೋಜನೆ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.",
                "Shishu up to ₹50,000; Kishor above ₹50,000 to ₹5 lakh; Tarun above ₹5 lakh to ₹10 lakh; Tarun Plus above ₹10 lakh to ₹20 lakh for eligible repeat borrowers.": "ಶಿಶು ₹50,000 ವರೆಗೆ; ಕಿಶೋರ್ ₹50,000 ಕ್ಕಿಂತ ಹೆಚ್ಚು ₹5 ಲಕ್ಷದವರೆಗೆ; ತರುಣ ₹5 ಲಕ್ಷಕ್ಕಿಂತ ಹೆಚ್ಚು ₹10 ಲಕ್ಷದವರೆಗೆ; ಅರ್ಹ ಮರುಸಾಲಗಾರರಿಗೆ ತರುಣ್ ಪ್ಲಸ್ ₹10 ಲಕ್ಷದಿಂದ ₹20 ಲಕ್ಷದವರೆಗೆ.",
                "Loan tranches can go up to ₹15,000, ₹25,000 and ₹50,000, subject to scheme conditions. Lending period has been extended to March 31, 2030.": "ಯೋಜನೆಯ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಸಾಲದ ಹಂತಗಳು ₹15,000, ₹25,000 ಮತ್ತು ₹50,000 ವರೆಗೆ ಇರಬಹುದು. ಸಾಲ ನೀಡುವ ಅವಧಿಯನ್ನು ಮಾರ್ಚ್ 31, 2030 ರವರೆಗೆ ವಿಸ್ತರಿಸಲಾಗಿದೆ.",
                "Individual micro food-processing units may receive 35% credit-linked capital subsidy up to ₹10 lakh, subject to eligibility and guidelines.": "ಅರ್ಹತೆ ಮತ್ತು ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಒಳಪಟ್ಟು ವೈಯಕ್ತಿಕ ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕಗಳಿಗೆ ₹10 ಲಕ್ಷದವರೆಗೆ 35% ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ದೊರೆಯಬಹುದು.",
                "Can support eligible crop and allied agricultural credit requirements through participating financial institutions.": "ಭಾಗವಹಿಸುವ ಹಣಕಾಸು ಸಂಸ್ಥೆಗಳ ಮೂಲಕ ಅರ್ಹ ಬೆಳೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಸಾಲ ಅಗತ್ಯಗಳಿಗೆ ಬೆಂಬಲ ನೀಡಬಹುದು.",
                "Eligible loans can receive interest subvention of 3% per year on the loan component up to ₹2 crore, subject to scheme conditions.": "ಯೋಜನೆಯ ಷರತ್ತುಗಳಿಗೆ ಒಳಪಟ್ಟು ಅರ್ಹ ಸಾಲದ ₹2 ಕೋಟಿವರೆಗಿನ ಸಾಲ ಘಟಕದ ಮೇಲೆ ವರ್ಷಕ್ಕೆ 3% ಬಡ್ಡಿ ಸಹಾಯ ದೊರೆಯಬಹುದು.",
                "Eligibility, training, project cost and subsidy provisions depend on the current ACABC guidelines.": "ಅರ್ಹತೆ, ತರಬೇತಿ, ಯೋಜನಾ ವೆಚ್ಚ ಮತ್ತು ಸಬ್ಸಿಡಿ ನಿಯಮಗಳು ಪ್ರಸ್ತುತ ACABC ಮಾರ್ಗಸೂಚಿಗಳ ಮೇಲೆ ಅವಲಂಬಿತವಾಗಿವೆ.",
                "Support is delivered through the rural livelihood mission structure and applicable state-level mechanisms.": "ಬೆಂಬಲವನ್ನು ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಮಿಷನ್ ವ್ಯವಸ್ಥೆ ಮತ್ತು ಅನ್ವಯಿಸುವ ರಾಜ್ಯ ಮಟ್ಟದ ವ್ಯವಸ್ಥೆಗಳ ಮೂಲಕ ನೀಡಲಾಗುತ್ತದೆ.",
                "Benefits and eligible trades are subject to the official scheme guidelines.": "ಲಾಭಗಳು ಮತ್ತು ಅರ್ಹ ವೃತ್ತಿಗಳು ಅಧಿಕೃತ ಯೋಜನಾ ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತವೆ.",
                "Component, subsidy and implementation conditions vary and are administered through the relevant authorities.": "ಘಟಕ, ಸಬ್ಸಿಡಿ ಮತ್ತು ಅನುಷ್ಠಾನದ ಷರತ್ತುಗಳು ಬದಲಾಗಬಹುದು ಮತ್ತು ಸಂಬಂಧಿತ ಅಧಿಕಾರಿಗಳ ಮೂಲಕ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ."
            },
            "why": {
                "Useful when the entrepreneur is starting a new eligible micro-enterprise and needs structured project finance.": "ಉದ್ಯಮಿಯು ಹೊಸ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮವನ್ನು ಆರಂಭಿಸುತ್ತಿರುವಾಗ ಮತ್ತು ಯೋಜಿತ ಹಣಕಾಸಿನ ಅಗತ್ಯವಿರುವಾಗ ಉಪಯುಕ್ತ.",
                "Useful for shops, services, food businesses, livestock-related activities and other eligible micro businesses.": "ಅಂಗಡಿಗಳು, ಸೇವೆಗಳು, ಆಹಾರ ವ್ಯವಹಾರಗಳು, ಜಾನುವಾರು ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು ಮತ್ತು ಇತರ ಅರ್ಹ ಸಣ್ಣ ವ್ಯವಹಾರಗಳಿಗೆ ಉಪಯುಕ್ತ.",
                "Especially relevant for small street food, vending and mobile retail businesses.": "ಸಣ್ಣ ಸ್ಟ್ರೀಟ್ ಫುಡ್, ಬೀದಿ ವ್ಯಾಪಾರ ಮತ್ತು ಮೊಬೈಲ್ ಚಿಲ್ಲರೆ ವ್ಯವಹಾರಗಳಿಗೆ ವಿಶೇಷವಾಗಿ ಉಪಯುಕ್ತ.",
                "A strong match for spice processing, pickles, snacks, flour, local food products and value-added agricultural produce.": "ಮಸಾಲೆ ಸಂಸ್ಕರಣೆ, ಉಪ್ಪಿನಕಾಯಿ, ತಿಂಡಿಗಳು, ಹಿಟ್ಟು, ಸ್ಥಳೀಯ ಆಹಾರ ಉತ್ಪನ್ನಗಳು ಮತ್ತು ಮೌಲ್ಯವರ್ಧಿತ ಕೃಷಿ ಉತ್ಪನ್ನಗಳಿಗೆ ಉತ್ತಮವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
                "Useful when the main business is farming or an eligible allied agricultural activity.": "ಮುಖ್ಯ ವ್ಯವಹಾರ ಕೃಷಿ ಅಥವಾ ಅರ್ಹ ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಯಾಗಿರುವಾಗ ಉಪಯುಕ್ತ.",
                "Useful for storage, grading, primary processing and other eligible agricultural infrastructure.": "ಸಂಗ್ರಹಣೆ, ವರ್ಗೀಕರಣ, ಪ್ರಾಥಮಿಕ ಸಂಸ್ಕರಣೆ ಮತ್ತು ಇತರ ಅರ್ಹ ಕೃಷಿ ಮೂಲಸೌಕರ್ಯಗಳಿಗೆ ಉಪಯುಕ್ತ.",
                "Useful for agriculture advisory, farm services, input-related services and other eligible agri-business models.": "ಕೃಷಿ ಸಲಹೆ, ಕೃಷಿ ಸೇವೆಗಳು, ಇನ್‌ಪುಟ್ ಸಂಬಂಧಿತ ಸೇವೆಗಳು ಮತ್ತು ಇತರ ಅರ್ಹ ಕೃಷಿ ವ್ಯವಹಾರ ಮಾದರಿಗಳಿಗೆ ಉಪಯುಕ್ತ.",
                "Useful for group enterprises, food processing, handicrafts and other SHG-based rural businesses.": "ಗುಂಪು ಉದ್ಯಮಗಳು, ಆಹಾರ ಸಂಸ್ಕರಣೆ, ಕರಕುಶಲ ಮತ್ತು ಇತರ SHG ಆಧಾರಿತ ಗ್ರಾಮೀಣ ವ್ಯವಹಾರಗಳಿಗೆ ಉಪಯುಕ್ತ.",
                "Relevant to tailoring and eligible traditional craft/artisan businesses.": "ಹೊಲಿಗೆ ಮತ್ತು ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕರಕುಶಲ/ಕುಶಲಕರ್ಮಿ ವ್ಯವಹಾರಗಳಿಗೆ ಸಂಬಂಧಿಸಿದೆ.",
                "Relevant where reliable agricultural energy and irrigation are important to the business model.": "ವಿಶ್ವಾಸಾರ್ಹ ಕೃಷಿ ಶಕ್ತಿ ಮತ್ತು ನೀರಾವರಿ ವ್ಯವಹಾರ ಮಾದರಿಗೆ ಮುಖ್ಯವಾಗಿರುವಲ್ಲಿ ಉಪಯುಕ್ತ."
            },
            "source": {
                "KVIC / Ministry of MSME": "KVIC / ಸೂಕ್ಷ್ಮ, ಸಣ್ಣ ಮತ್ತು ಮಧ್ಯಮ ಉದ್ಯಮಗಳ ಸಚಿವಾಲಯ",
                "Department of Financial Services, Ministry of Finance": "ಹಣಕಾಸು ಸೇವೆಗಳ ಇಲಾಖೆ, ಹಣಕಾಸು ಸಚಿವಾಲಯ",
                "Ministry of Housing & Urban Affairs / Government of India": "ವಸತಿ ಮತ್ತು ನಗರ ವ್ಯವಹಾರಗಳ ಸಚಿವಾಲಯ / ಭಾರತ ಸರ್ಕಾರ",
                "Ministry of Food Processing Industries": "ಆಹಾರ ಸಂಸ್ಕರಣಾ ಕೈಗಾರಿಕೆಗಳ ಸಚಿವಾಲಯ",
                "Government of India / Department of Financial Services": "ಭಾರತ ಸರ್ಕಾರ / ಹಣಕಾಸು ಸೇವೆಗಳ ಇಲಾಖೆ",
                "Department of Agriculture & Farmers Welfare": "ಕೃಷಿ ಮತ್ತು ರೈತರ ಕಲ್ಯಾಣ ಇಲಾಖೆ",
                "MANAGE / Ministry of Agriculture & Farmers Welfare": "MANAGE / ಕೃಷಿ ಮತ್ತು ರೈತರ ಕಲ್ಯಾಣ ಸಚಿವಾಲಯ",
                "Ministry of Rural Development": "ಗ್ರಾಮೀಣ ಅಭಿವೃದ್ಧಿ ಸಚಿವಾಲಯ",
                "Government of India": "ಭಾರತ ಸರ್ಕಾರ",
                "Ministry of New and Renewable Energy": "ಹೊಸ ಮತ್ತು ನವೀಕರಿಸಬಹುದಾದ ಇಂಧನ ಸಚಿವಾಲಯ"
            }
        }
    }

    def stext(kind, value):
        return SCHEME_TR.get(language, {}).get(kind, {}).get(value, value)

    def scheme_name(value):
        return SCHEME_NAME_TR.get(language, {}).get(value, value)

    def scheme_extra(kind, value):
        return SCHEME_EXTRA_TR.get(language, {}).get(kind, {}).get(value, value)

    for scheme in shown:
        with st.expander(scheme_name(scheme["name"])):
            st.markdown(f"**{tr('best_for')}:** {stext('best', scheme['best_for'])}")
            st.write(stext('desc', scheme["description"]))
            st.markdown(f"**{tr('key')}:** {scheme_extra('key', scheme['key'])}")
            st.markdown(f"**{tr('why')}:** {scheme_extra('why', scheme['why'])}")
            st.caption(f"{tr('source')}: {scheme_extra('source', scheme['source'])}")

    st.warning(tr("scheme_warning"))

# ============================================================
# FINANCIAL ASSISTANT
# ============================================================

if page == "Financial Assistant":
    st.title("💰 " + tr("finance_title"))
    tab1, tab2 = st.tabs([tr("profit_tab"), tr("emi_tab")])

    with tab1:
        st.subheader(tr("profit_est"))
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(tr("quantity"), min_value=1.0, value=100.0)
            purchase_price = st.number_input(tr("purchase"), min_value=0.0, value=20.0)
        with col2:
            selling_price = st.number_input(tr("selling"), min_value=0.0, value=30.0)
            other_costs = st.number_input(tr("other"), min_value=0.0, value=0.0)

        total_cost = quantity * purchase_price + other_costs
        revenue = quantity * selling_price
        profit = revenue - total_cost

        a, b, c = st.columns(3)
        a.metric(tr("total_cost"), money(total_cost))
        b.metric(tr("revenue"), money(revenue))
        c.metric(tr("profit"), money(profit))

        if profit > 0:
            st.success(tr("positive"))
        elif profit == 0:
            st.info(tr("break_even"))
        else:
            st.error(tr("loss"))

    with tab2:
        st.subheader(tr("emi_tab").replace("🏦 ", ""))
        col1, col2, col3 = st.columns(3)
        with col1:
            principal = st.number_input(tr("loan"), min_value=1000.0, value=100000.0, step=5000.0)
        with col2:
            annual_rate = st.number_input(tr("rate"), min_value=0.0, value=10.0, step=0.5)
        with col3:
            years = st.number_input(tr("period"), min_value=1, value=3)

        months = years * 12
        monthly_rate = annual_rate / 12 / 100
        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

        total_payment = emi * months
        total_interest = total_payment - principal

        a, b, c = st.columns(3)
        a.metric(tr("monthly"), money(emi))
        b.metric(tr("total_payment"), money(total_payment))
        c.metric(tr("interest"), money(total_interest))
        st.caption(tr("loan_note"))

# ============================================================
# BUSINESS RECOMMENDATION
# ============================================================

if page == "Business Recommendation":
    st.title("💡 " + tr("business_title"))
    st.write(tr("business_desc"))

    col1, col2 = st.columns(2)

    resource_values = [
        "Land", "Water", "Shop space", "Kitchen/Workspace", "Cattle",
        "Sewing machine", "Vehicle", "Repair tools", "Craft skills",
        "Agriculture knowledge", "Not sure / I have limited resources"
    ]
    interest_values = [
        "Farming", "Agriculture", "Vegetables", "Food", "Cooking", "Retail",
        "Livestock", "Poultry", "Dairy", "Transport", "Delivery", "Tailoring",
        "Handicrafts", "Repair", "Technology", "General business"
    ]

    RESOURCE_TR = {
        "Hindi": {"Land":"ज़मीन","Water":"पानी","Shop space":"दुकान की जगह","Kitchen/Workspace":"रसोई/कार्यस्थल","Cattle":"पशु","Sewing machine":"सिलाई मशीन","Vehicle":"वाहन","Repair tools":"मरम्मत के औज़ार","Craft skills":"कारीगरी कौशल","Agriculture knowledge":"कृषि ज्ञान","Not sure / I have limited resources":"पता नहीं / मेरे पास सीमित संसाधन हैं"},
        "Kannada": {"Land":"ಭೂಮಿ","Water":"ನೀರು","Shop space":"ಅಂಗಡಿ ಸ್ಥಳ","Kitchen/Workspace":"ಅಡುಗೆಮನೆ/ಕೆಲಸದ ಸ್ಥಳ","Cattle":"ಜಾನುವಾರು","Sewing machine":"ಹೊಲಿಗೆ ಯಂತ್ರ","Vehicle":"ವಾಹನ","Repair tools":"ದುರಸ್ತಿ ಉಪಕರಣಗಳು","Craft skills":"ಕರಕುಶಲ ಕೌಶಲ್ಯ","Agriculture knowledge":"ಕೃಷಿ ಜ್ಞಾನ","Not sure / I have limited resources":"ಖಚಿತವಿಲ್ಲ / ನನ್ನ ಬಳಿ ಸೀಮಿತ ಸಂಪನ್ಮೂಲಗಳಿವೆ"}
    }
    INTEREST_TR = {
        "Hindi": {"Farming":"खेती","Agriculture":"कृषि","Vegetables":"सब्ज़ियाँ","Food":"भोजन","Cooking":"खाना बनाना","Retail":"खुदरा","Livestock":"पशुपालन","Poultry":"पोल्ट्री","Dairy":"डेयरी","Transport":"परिवहन","Delivery":"डिलीवरी","Tailoring":"सिलाई","Handicrafts":"हस्तशिल्प","Repair":"मरम्मत","Technology":"तकनीक","General business":"सामान्य व्यवसाय"},
        "Kannada": {"Farming":"ಕೃಷಿ","Agriculture":"ಕೃಷಿ","Vegetables":"ತರಕಾರಿಗಳು","Food":"ಆಹಾರ","Cooking":"ಅಡುಗೆ","Retail":"ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರ","Livestock":"ಪಶುಸಂಗೋಪನೆ","Poultry":"ಕೋಳಿ ಸಾಕಣೆ","Dairy":"ಡೈರಿ","Transport":"ಸಾರಿಗೆ","Delivery":"ವಿತರಣೆ","Tailoring":"ಹೊಲಿಗೆ","Handicrafts":"ಕರಕುಶಲ","Repair":"ದುರಸ್ತಿ","Technology":"ತಂತ್ರಜ್ಞಾನ","General business":"ಸಾಮಾನ್ಯ ವ್ಯವಹಾರ"}
    }

    # ---------------------------------------------------------
    # USER INPUTS
    # IMPORTANT: these variables must be created BEFORE the
    # recommendation button uses calculate_match().
    # ---------------------------------------------------------
    with col1:
        capital = st.number_input(
            tr("capital"),
            min_value=0.0,
            value=100000.0,
            step=5000.0,
            format="%.0f"
        )

        resource = st.selectbox(
            tr("resource"),
            resource_values,
            format_func=lambda x: RESOURCE_TR.get(language, {}).get(x, x)
        )

        interest = st.selectbox(
            tr("interest_input"),
            interest_values,
            format_func=lambda x: INTEREST_TR.get(language, {}).get(x, x)
        )

    with col2:
        water = st.selectbox(
            tr("water"),
            ["Good", "Limited", "Not applicable"],
            format_func=lambda x: {
                "Good": tr("good"),
                "Limited": tr("limited"),
                "Not applicable": tr("not_applicable")
            }[x]
        )

        experience = st.selectbox(
            tr("experience"),
            ["Beginner", "Some experience", "Experienced"],
            format_func=lambda x: {
                "Beginner": tr("beginner"),
                "Some experience": tr("some"),
                "Experienced": tr("experienced")
            }[x]
        )

    st.info(tr("location_note", location=location))

    # ---------------------------------------------------------
    # COMPLETE BUSINESS CONTENT TRANSLATIONS
    # These dictionaries translate the content stored in BUSINESSES
    # while keeping the English values internally for scoring.
    # ---------------------------------------------------------
    BUSINESS_CONTENT_TR = {
        "Hindi": {
            "investment": {
                "₹25,000 – ₹2.5 lakh": "₹25,000 – ₹2.5 लाख",
                "₹75,000 – ₹10 lakh+": "₹75,000 – ₹10 लाख+",
                "₹1 lakh – ₹7 lakh": "₹1 लाख – ₹7 लाख",
                "₹30,000 – ₹3 lakh": "₹30,000 – ₹3 लाख",
                "₹1 lakh – ₹8 lakh": "₹1 लाख – ₹8 लाख",
                "₹60,000 – ₹5 lakh": "₹60,000 – ₹5 लाख",
                "₹80,000 – ₹6 lakh": "₹80,000 – ₹6 लाख",
                "₹75,000 – ₹6 lakh": "₹75,000 – ₹6 लाख",
                "₹30,000 – ₹2.5 lakh": "₹30,000 – ₹2.5 लाख",
                "₹25,000 – ₹3 lakh": "₹25,000 – ₹3 लाख",
                "₹1.5 lakh – ₹10 lakh+": "₹1.5 लाख – ₹10 लाख+",
                "₹40,000 – ₹3 lakh": "₹40,000 – ₹3 लाख"
            },
            "model": {
                "Grow vegetables → sell to local markets, retailers, hotels or direct customers.": "सब्ज़ियाँ उगाएँ → स्थानीय बाजारों, खुदरा विक्रेताओं, होटलों या सीधे ग्राहकों को बेचें।",
                "Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.": "स्थानीय उपज को आटा, स्नैक्स, अचार, मसाला मिश्रण या पैकेज्ड खाद्य जैसे अधिक मूल्य वाले उत्पादों में बदलें।",
                "Sell essential household products with repeat local demand.": "नियमित स्थानीय मांग वाले आवश्यक घरेलू उत्पाद बेचें।",
                "Sell affordable snacks or meals at a high-footfall local location.": "अधिक ग्राहक आने वाली स्थानीय जगह पर किफायती स्नैक्स या भोजन बेचें।",
                "Milk production with possible value addition such as curd, paneer or ghee.": "दूध का उत्पादन करें और दही, पनीर या घी जैसे मूल्यवर्धित उत्पाद बनाएं।",
                "Rear animals for meat, breeding or local livestock markets.": "मांस, प्रजनन या स्थानीय पशु बाजारों के लिए पशुओं का पालन करें।",
                "Egg or broiler production for nearby markets.": "नजदीकी बाजारों के लिए अंडे या ब्रॉयलर का उत्पादन करें।",
                "Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.": "नजदीकी गांवों/कस्बों में किराना, कृषि इनपुट, दवाइयाँ या स्थानीय सामान पहुँचाएँ।",
                "Alterations, stitching, school uniforms, traditional clothing and small-batch garments.": "कपड़ों की अल्टरशन, सिलाई, स्कूल यूनिफॉर्म, पारंपरिक कपड़े और छोटे बैच के परिधान तैयार करें।",
                "Make baskets, decor, traditional products or locally distinctive handmade goods.": "टोकरी, सजावटी सामान, पारंपरिक उत्पाद या स्थानीय विशेषता वाले हस्तनिर्मित सामान बनाएँ।",
                "Supply seeds, tools, irrigation accessories and farm-related services.": "बीज, उपकरण, सिंचाई सामग्री और कृषि संबंधी सेवाएँ उपलब्ध कराएँ।",
                "Repair phones, appliances, agricultural equipment or other locally needed items.": "मोबाइल, उपकरण, कृषि मशीनरी या स्थानीय रूप से आवश्यक अन्य वस्तुओं की मरम्मत करें।"
            },
            "risk": {
                "Weather, water availability and price fluctuations.": "मौसम, पानी की उपलब्धता और कीमतों में उतार-चढ़ाव।",
                "Food safety, packaging, shelf life and market access.": "खाद्य सुरक्षा, पैकेजिंग, शेल्फ लाइफ और बाजार तक पहुँच।",
                "Competition, inventory management and credit sales.": "प्रतिस्पर्धा, स्टॉक प्रबंधन और उधार बिक्री।",
                "Location dependency, hygiene and daily demand variation.": "स्थान पर निर्भरता, स्वच्छता और दैनिक मांग में बदलाव।",
                "Animal health, feed costs and milk-price changes.": "पशु स्वास्थ्य, चारे की लागत और दूध की कीमतों में बदलाव।",
                "Disease, feed costs and market-price fluctuations.": "बीमारी, चारे की लागत और बाजार कीमतों में उतार-चढ़ाव।",
                "Feed costs, disease and price volatility.": "चारे की लागत, बीमारी और कीमतों में अस्थिरता।",
                "Fuel costs, vehicle maintenance and route density.": "ईंधन की लागत, वाहन रखरखाव और मार्ग की मांग।",
                "Competition and seasonal demand.": "प्रतिस्पर्धा और मौसमी मांग।",
                "Demand discovery and inconsistent order volume.": "मांग का पता लगाना और ऑर्डर की मात्रा में अस्थिरता।",
                "Inventory, licensing requirements and seasonal demand.": "स्टॉक, लाइसेंस की आवश्यकताएँ और मौसमी मांग।",
                "Skill dependency and availability of spare parts.": "कौशल पर निर्भरता और स्पेयर पार्ट्स की उपलब्धता।"
            },
            "steps": {
                "Select crops based on local demand and water availability.": "स्थानीय मांग और पानी की उपलब्धता के आधार पर फसलें चुनें।",
                "Estimate seed, labour, irrigation and transport costs.": "बीज, श्रम, सिंचाई और परिवहन की लागत का अनुमान लगाएँ।",
                "Plan more than one sales channel instead of depending on a single buyer.": "एक ही खरीदार पर निर्भर रहने के बजाय एक से अधिक बिक्री चैनल रखें।",
                "Choose one product with a clear local customer segment.": "स्पष्ट स्थानीय ग्राहक वर्ग वाला एक उत्पाद चुनें।",
                "Calculate raw material, packaging, labour and selling costs.": "कच्चे माल, पैकेजिंग, श्रम और बिक्री लागत की गणना करें।",
                "Test a small batch before investing in larger equipment.": "बड़े उपकरणों में निवेश करने से पहले छोटे बैच का परीक्षण करें।",
                "Start with fast-moving essentials instead of excessive inventory.": "अधिक स्टॉक रखने के बजाय तेजी से बिकने वाली आवश्यक वस्तुओं से शुरुआत करें।",
                "Track daily sales and stock movement.": "दैनिक बिक्री और स्टॉक की आवाजाही का रिकॉर्ड रखें।",
                "Add high-demand local products after observing customer behaviour.": "ग्राहकों के व्यवहार को देखकर अधिक मांग वाले स्थानीय उत्पाद जोड़ें।",
                "Choose a small menu with good margins.": "अच्छे मार्जिन वाला छोटा मेन्यू चुनें।",
                "Test demand at different times of the day.": "दिन के अलग-अलग समय पर मांग का परीक्षण करें।",
                "Maintain hygiene, consistent quality and simple bookkeeping.": "स्वच्छता, समान गुणवत्ता और सरल लेखा-जोखा बनाए रखें।",
                "Estimate feed and veterinary costs before buying animals.": "पशु खरीदने से पहले चारे और पशु चिकित्सा की लागत का अनुमान लगाएँ।",
                "Identify a reliable local milk buyer.": "एक भरोसेमंद स्थानीय दूध खरीदार की पहचान करें।",
                "Maintain records of milk yield and animal health.": "दूध उत्पादन और पशु स्वास्थ्य का रिकॉर्ड रखें।",
                "Start with a manageable herd size.": "संभालने योग्य झुंड के आकार से शुरुआत करें।",
                "Plan vaccination and veterinary care.": "टीकाकरण और पशु चिकित्सा देखभाल की योजना बनाएँ।",
                "Build a buyer network before scaling.": "विस्तार करने से पहले खरीदारों का नेटवर्क बनाएँ।",
                "Choose egg or meat production based on local demand.": "स्थानीय मांग के आधार पर अंडा या मांस उत्पादन चुनें।",
                "Calculate feed cost per bird.": "प्रति पक्षी चारे की लागत की गणना करें।",
                "Maintain biosecurity and veterinary schedules.": "जैव-सुरक्षा और पशु चिकित्सा कार्यक्रम बनाए रखें।",
                "Map villages and shops that need regular delivery.": "नियमित डिलीवरी की जरूरत वाले गांवों और दुकानों की सूची बनाएँ।",
                "Start with a defined service radius.": "एक निश्चित सेवा क्षेत्र से शुरुआत करें।",
                "Use simple digital records for orders, fuel and collections.": "ऑर्डर, ईंधन और भुगतान संग्रह के लिए सरल डिजिटल रिकॉर्ड रखें।",
                "Start with alterations and high-demand local garments.": "अल्टरशन और अधिक मांग वाले स्थानीय परिधानों से शुरुआत करें।",
                "Build repeat customers through reliable delivery.": "विश्वसनीय सेवा देकर नियमित ग्राहकों का आधार बनाएँ।",
                "Add machines only when order volume justifies them.": "ऑर्डर की मात्रा पर्याप्त होने पर ही मशीनें बढ़ाएँ।",
                "Create a small catalogue and sample products.": "एक छोटा कैटलॉग और नमूना उत्पाद तैयार करें।",
                "Explore local fairs, retailers and digital selling channels.": "स्थानीय मेलों, खुदरा विक्रेताओं और डिजिटल बिक्री चैनलों का उपयोग करें।",
                "Identify the crops and farm needs of nearby villages.": "नजदीकी गांवों की फसलों और कृषि जरूरतों की पहचान करें।",
                "Stock fast-moving inputs first.": "पहले तेजी से बिकने वाले कृषि इनपुट रखें।",
                "Follow all applicable licences and quality requirements.": "सभी लागू लाइसेंस और गुणवत्ता आवश्यकताओं का पालन करें।",
                "Choose one repair category based on local demand.": "स्थानीय मांग के आधार पर एक मरम्मत श्रेणी चुनें।",
                "Keep commonly required spare parts.": "आमतौर पर आवश्यक स्पेयर पार्ट्स रखें।",
                "Build trust through transparent pricing and service records.": "पारदर्शी कीमत और सेवा रिकॉर्ड के माध्यम से भरोसा बनाएँ।"
            }
        },
        "Kannada": {
            "investment": {
                "₹25,000 – ₹2.5 lakh": "₹25,000 – ₹2.5 ಲಕ್ಷ",
                "₹75,000 – ₹10 lakh+": "₹75,000 – ₹10 ಲಕ್ಷ+",
                "₹1 lakh – ₹7 lakh": "₹1 ಲಕ್ಷ – ₹7 ಲಕ್ಷ",
                "₹30,000 – ₹3 lakh": "₹30,000 – ₹3 ಲಕ್ಷ",
                "₹1 lakh – ₹8 lakh": "₹1 ಲಕ್ಷ – ₹8 ಲಕ್ಷ",
                "₹60,000 – ₹5 lakh": "₹60,000 – ₹5 ಲಕ್ಷ",
                "₹80,000 – ₹6 lakh": "₹80,000 – ₹6 ಲಕ್ಷ",
                "₹75,000 – ₹6 lakh": "₹75,000 – ₹6 ಲಕ್ಷ",
                "₹30,000 – ₹2.5 lakh": "₹30,000 – ₹2.5 ಲಕ್ಷ",
                "₹25,000 – ₹3 lakh": "₹25,000 – ₹3 ಲಕ್ಷ",
                "₹1.5 lakh – ₹10 lakh+": "₹1.5 ಲಕ್ಷ – ₹10 ಲಕ್ಷ+",
                "₹40,000 – ₹3 lakh": "₹40,000 – ₹3 ಲಕ್ಷ"
            },
            "model": {
                "Grow vegetables → sell to local markets, retailers, hotels or direct customers.": "ತರಕಾರಿಗಳನ್ನು ಬೆಳೆಸಿ → ಸ್ಥಳೀಯ ಮಾರುಕಟ್ಟೆಗಳು, ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರಿಗಳು, ಹೋಟೆಲ್‌ಗಳು ಅಥವಾ ನೇರ ಗ್ರಾಹಕರಿಗೆ ಮಾರಾಟ ಮಾಡಿ.",
                "Convert local produce into higher-value products such as flour, snacks, pickles, spice mixes or packaged foods.": "ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳನ್ನು ಹಿಟ್ಟು, ತಿಂಡಿಗಳು, ಉಪ್ಪಿನಕಾಯಿ, ಮಸಾಲೆ ಮಿಶ್ರಣಗಳು ಅಥವಾ ಪ್ಯಾಕೇಜ್ ಮಾಡಿದ ಆಹಾರದಂತಹ ಹೆಚ್ಚಿನ ಮೌಲ್ಯದ ಉತ್ಪನ್ನಗಳಾಗಿ ಪರಿವರ್ತಿಸಿ.",
                "Sell essential household products with repeat local demand.": "ನಿರಂತರ ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯಿರುವ ಅಗತ್ಯ ಗೃಹೋಪಯೋಗಿ ಉತ್ಪನ್ನಗಳನ್ನು ಮಾರಾಟ ಮಾಡಿ.",
                "Sell affordable snacks or meals at a high-footfall local location.": "ಹೆಚ್ಚು ಜನ ಸಂಚಾರವಿರುವ ಸ್ಥಳದಲ್ಲಿ ಕೈಗೆಟುಕುವ ತಿಂಡಿಗಳು ಅಥವಾ ಊಟವನ್ನು ಮಾರಾಟ ಮಾಡಿ.",
                "Milk production with possible value addition such as curd, paneer or ghee.": "ಹಾಲು ಉತ್ಪಾದಿಸಿ ಮತ್ತು ಮೊಸರು, ಪನೀರ್ ಅಥವಾ ತುಪ್ಪದಂತಹ ಮೌಲ್ಯವರ್ಧಿತ ಉತ್ಪನ್ನಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Rear animals for meat, breeding or local livestock markets.": "ಮಾಂಸ, ಸಂತಾನೋತ್ಪತ್ತಿ ಅಥವಾ ಸ್ಥಳೀಯ ಜಾನುವಾರು ಮಾರುಕಟ್ಟೆಗಳಿಗಾಗಿ ಪ್ರಾಣಿಗಳನ್ನು ಸಾಕಿ.",
                "Egg or broiler production for nearby markets.": "ಹತ್ತಿರದ ಮಾರುಕಟ್ಟೆಗಳಿಗಾಗಿ ಮೊಟ್ಟೆ ಅಥವಾ ಬ್ರಾಯ್ಲರ್ ಉತ್ಪಾದನೆ ಮಾಡಿ.",
                "Deliver groceries, farm inputs, medicines or local goods within nearby villages/towns.": "ಹತ್ತಿರದ ಗ್ರಾಮಗಳು/ಪಟ್ಟಣಗಳಲ್ಲಿ ದಿನಸಿ, ಕೃಷಿ ಇನ್‌ಪುಟ್‌ಗಳು, ಔಷಧಿಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ಸರಕುಗಳನ್ನು ವಿತರಿಸಿ.",
                "Alterations, stitching, school uniforms, traditional clothing and small-batch garments.": "ಬಟ್ಟೆ ಬದಲಾವಣೆ, ಹೊಲಿಗೆ, ಶಾಲಾ ಸಮವಸ್ತ್ರ, ಸಾಂಪ್ರದಾಯಿಕ ಉಡುಪುಗಳು ಮತ್ತು ಸಣ್ಣ ಪ್ರಮಾಣದ ಉಡುಪುಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Make baskets, decor, traditional products or locally distinctive handmade goods.": "ಬುಟ್ಟಿಗಳು, ಅಲಂಕಾರಿಕ ವಸ್ತುಗಳು, ಸಾಂಪ್ರದಾಯಿಕ ಉತ್ಪನ್ನಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ವಿಶೇಷತೆಯ ಕೈತಯಾರಿಕಾ ವಸ್ತುಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Supply seeds, tools, irrigation accessories and farm-related services.": "ಬೀಜಗಳು, ಉಪಕರಣಗಳು, ನೀರಾವರಿ ಸಾಮಗ್ರಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಬಂಧಿತ ಸೇವೆಗಳನ್ನು ಒದಗಿಸಿ.",
                "Repair phones, appliances, agricultural equipment or other locally needed items.": "ಮೊಬೈಲ್‌ಗಳು, ಉಪಕರಣಗಳು, ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳು ಅಥವಾ ಸ್ಥಳೀಯವಾಗಿ ಅಗತ್ಯವಿರುವ ಇತರ ವಸ್ತುಗಳನ್ನು ದುರಸ್ತಿ ಮಾಡಿ."
            },
            "risk": {
                "Weather, water availability and price fluctuations.": "ಹವಾಮಾನ, ನೀರಿನ ಲಭ್ಯತೆ ಮತ್ತು ಬೆಲೆ ಏರಿಳಿತಗಳು.",
                "Food safety, packaging, shelf life and market access.": "ಆಹಾರ ಸುರಕ್ಷತೆ, ಪ್ಯಾಕೇಜಿಂಗ್, ಸಂಗ್ರಹ ಅವಧಿ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಪ್ರವೇಶ.",
                "Competition, inventory management and credit sales.": "ಸ್ಪರ್ಧೆ, ದಾಸ್ತಾನು ನಿರ್ವಹಣೆ ಮತ್ತು ಸಾಲದ ಮಾರಾಟ.",
                "Location dependency, hygiene and daily demand variation.": "ಸ್ಥಳದ ಅವಲಂಬನೆ, ಸ್ವಚ್ಛತೆ ಮತ್ತು ದೈನಂದಿನ ಬೇಡಿಕೆಯ ಬದಲಾವಣೆ.",
                "Animal health, feed costs and milk-price changes.": "ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯ, ಮೇವು ವೆಚ್ಚ ಮತ್ತು ಹಾಲಿನ ಬೆಲೆ ಬದಲಾವಣೆಗಳು.",
                "Disease, feed costs and market-price fluctuations.": "ರೋಗ, ಮೇವು ವೆಚ್ಚ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಏರಿಳಿತಗಳು.",
                "Feed costs, disease and price volatility.": "ಮೇವು ವೆಚ್ಚ, ರೋಗ ಮತ್ತು ಬೆಲೆ ಅಸ್ಥಿರತೆ.",
                "Fuel costs, vehicle maintenance and route density.": "ಇಂಧನ ವೆಚ್ಚ, ವಾಹನ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾರ್ಗದ ಬೇಡಿಕೆ.",
                "Competition and seasonal demand.": "ಸ್ಪರ್ಧೆ ಮತ್ತು ಋತುಮಾನ ಬೇಡಿಕೆ.",
                "Demand discovery and inconsistent order volume.": "ಬೇಡಿಕೆಯನ್ನು ಗುರುತಿಸುವುದು ಮತ್ತು ಆರ್ಡರ್ ಪ್ರಮಾಣದ ಅಸ್ಥಿರತೆ.",
                "Inventory, licensing requirements and seasonal demand.": "ದಾಸ್ತಾನು, ಪರವಾನಗಿ ಅಗತ್ಯತೆಗಳು ಮತ್ತು ಋತುಮಾನ ಬೇಡಿಕೆ.",
                "Skill dependency and availability of spare parts.": "ಕೌಶಲ್ಯದ ಅವಲಂಬನೆ ಮತ್ತು ಸ್ಪೇರ್ ಪಾರ್ಟ್ಸ್ ಲಭ್ಯತೆ."
            },
            "steps": {
                "Select crops based on local demand and water availability.": "ಸ್ಥಳೀಯ ಬೇಡಿಕೆ ಮತ್ತು ನೀರಿನ ಲಭ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ಬೆಳೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Estimate seed, labour, irrigation and transport costs.": "ಬೀಜ, ಕಾರ್ಮಿಕ, ನೀರಾವರಿ ಮತ್ತು ಸಾರಿಗೆ ವೆಚ್ಚಗಳನ್ನು ಅಂದಾಜಿಸಿ.",
                "Plan more than one sales channel instead of depending on a single buyer.": "ಒಬ್ಬ ಖರೀದಿದಾರನ ಮೇಲೆ ಅವಲಂಬಿಸದೆ ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಮಾರಾಟ ಮಾರ್ಗಗಳನ್ನು ಯೋಜಿಸಿ.",
                "Choose one product with a clear local customer segment.": "ಸ್ಪಷ್ಟ ಸ್ಥಳೀಯ ಗ್ರಾಹಕ ವರ್ಗವಿರುವ ಒಂದು ಉತ್ಪನ್ನವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Calculate raw material, packaging, labour and selling costs.": "ಕಚ್ಚಾ ವಸ್ತು, ಪ್ಯಾಕೇಜಿಂಗ್, ಕಾರ್ಮಿಕ ಮತ್ತು ಮಾರಾಟ ವೆಚ್ಚಗಳನ್ನು ಲೆಕ್ಕಿಸಿ.",
                "Test a small batch before investing in larger equipment.": "ದೊಡ್ಡ ಉಪಕರಣಗಳಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡುವ ಮೊದಲು ಸಣ್ಣ ಬ್ಯಾಚ್ ಪರೀಕ್ಷಿಸಿ.",
                "Start with fast-moving essentials instead of excessive inventory.": "ಹೆಚ್ಚು ದಾಸ್ತಾನು ಇಡುವ ಬದಲು ವೇಗವಾಗಿ ಮಾರಾಟವಾಗುವ ಅಗತ್ಯ ವಸ್ತುಗಳಿಂದ ಆರಂಭಿಸಿ.",
                "Track daily sales and stock movement.": "ದೈನಂದಿನ ಮಾರಾಟ ಮತ್ತು ದಾಸ್ತಾನು ಚಲನವಲನವನ್ನು ದಾಖಲಿಸಿ.",
                "Add high-demand local products after observing customer behaviour.": "ಗ್ರಾಹಕರ ವರ್ತನೆಯನ್ನು ಗಮನಿಸಿದ ನಂತರ ಹೆಚ್ಚು ಬೇಡಿಕೆಯ ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳನ್ನು ಸೇರಿಸಿ.",
                "Choose a small menu with good margins.": "ಉತ್ತಮ ಲಾಭಾಂಶವಿರುವ ಸಣ್ಣ ಮೆನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Test demand at different times of the day.": "ದಿನದ ವಿವಿಧ ಸಮಯಗಳಲ್ಲಿ ಬೇಡಿಕೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ.",
                "Maintain hygiene, consistent quality and simple bookkeeping.": "ಸ್ವಚ್ಛತೆ, ಸ್ಥಿರ ಗುಣಮಟ್ಟ ಮತ್ತು ಸರಳ ಲೆಕ್ಕಪತ್ರವನ್ನು ಕಾಪಾಡಿ.",
                "Estimate feed and veterinary costs before buying animals.": "ಜಾನುವಾರುಗಳನ್ನು ಖರೀದಿಸುವ ಮೊದಲು ಮೇವು ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ವೆಚ್ಚಗಳನ್ನು ಅಂದಾಜಿಸಿ.",
                "Identify a reliable local milk buyer.": "ವಿಶ್ವಾಸಾರ್ಹ ಸ್ಥಳೀಯ ಹಾಲು ಖರೀದಿದಾರರನ್ನು ಗುರುತಿಸಿ.",
                "Maintain records of milk yield and animal health.": "ಹಾಲಿನ ಉತ್ಪಾದನೆ ಮತ್ತು ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯದ ದಾಖಲೆಗಳನ್ನು ಇಡಿ.",
                "Start with a manageable herd size.": "ನಿರ್ವಹಿಸಬಹುದಾದ ಹಿಂಡಿನ ಗಾತ್ರದಿಂದ ಆರಂಭಿಸಿ.",
                "Plan vaccination and veterinary care.": "ಲಸಿಕೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ಆರೈಕೆಯ ಯೋಜನೆ ಮಾಡಿ.",
                "Build a buyer network before scaling.": "ವಿಸ್ತರಿಸುವ ಮೊದಲು ಖರೀದಿದಾರರ ಜಾಲವನ್ನು ನಿರ್ಮಿಸಿ.",
                "Choose egg or meat production based on local demand.": "ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಮೊಟ್ಟೆ ಅಥವಾ ಮಾಂಸ ಉತ್ಪಾದನೆಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Calculate feed cost per bird.": "ಪ್ರತಿ ಪಕ್ಷಿಯ ಮೇವು ವೆಚ್ಚವನ್ನು ಲೆಕ್ಕಿಸಿ.",
                "Maintain biosecurity and veterinary schedules.": "ಜೈವಿಕ ಭದ್ರತೆ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಕಾಪಾಡಿ.",
                "Map villages and shops that need regular delivery.": "ನಿಯಮಿತ ವಿತರಣೆಯ ಅಗತ್ಯವಿರುವ ಗ್ರಾಮಗಳು ಮತ್ತು ಅಂಗಡಿಗಳನ್ನು ಗುರುತಿಸಿ.",
                "Start with a defined service radius.": "ನಿರ್ದಿಷ್ಟ ಸೇವಾ ವ್ಯಾಪ್ತಿಯಿಂದ ಆರಂಭಿಸಿ.",
                "Use simple digital records for orders, fuel and collections.": "ಆರ್ಡರ್‌ಗಳು, ಇಂಧನ ಮತ್ತು ಪಾವತಿ ಸಂಗ್ರಹಕ್ಕಾಗಿ ಸರಳ ಡಿಜಿಟಲ್ ದಾಖಲೆಗಳನ್ನು ಬಳಸಿ.",
                "Start with alterations and high-demand local garments.": "ಬಟ್ಟೆ ಬದಲಾವಣೆ ಮತ್ತು ಹೆಚ್ಚು ಬೇಡಿಕೆಯ ಸ್ಥಳೀಯ ಉಡುಪುಗಳಿಂದ ಆರಂಭಿಸಿ.",
                "Build repeat customers through reliable delivery.": "ವಿಶ್ವಾಸಾರ್ಹ ಸೇವೆಯ ಮೂಲಕ ಮರುಬರುವ ಗ್ರಾಹಕರನ್ನು ನಿರ್ಮಿಸಿ.",
                "Add machines only when order volume justifies them.": "ಆರ್ಡರ್ ಪ್ರಮಾಣವು ಸಮರ್ಥಿಸಿದಾಗ ಮಾತ್ರ ಯಂತ್ರಗಳನ್ನು ಹೆಚ್ಚಿಸಿ.",
                "Create a small catalogue and sample products.": "ಸಣ್ಣ ಕ್ಯಾಟಲಾಗ್ ಮತ್ತು ಮಾದರಿ ಉತ್ಪನ್ನಗಳನ್ನು ತಯಾರಿಸಿ.",
                "Explore local fairs, retailers and digital selling channels.": "ಸ್ಥಳೀಯ ಜಾತ್ರೆಗಳು, ಚಿಲ್ಲರೆ ವ್ಯಾಪಾರಿಗಳು ಮತ್ತು ಡಿಜಿಟಲ್ ಮಾರಾಟ ಮಾರ್ಗಗಳನ್ನು ಅನ್ವೇಷಿಸಿ.",
                "Identify the crops and farm needs of nearby villages.": "ಹತ್ತಿರದ ಗ್ರಾಮಗಳ ಬೆಳೆಗಳು ಮತ್ತು ಕೃಷಿ ಅಗತ್ಯಗಳನ್ನು ಗುರುತಿಸಿ.",
                "Stock fast-moving inputs first.": "ಮೊದಲು ವೇಗವಾಗಿ ಮಾರಾಟವಾಗುವ ಕೃಷಿ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ.",
                "Follow all applicable licences and quality requirements.": "ಅನ್ವಯವಾಗುವ ಎಲ್ಲಾ ಪರವಾನಗಿ ಮತ್ತು ಗುಣಮಟ್ಟದ ಅವಶ್ಯಕತೆಗಳನ್ನು ಪಾಲಿಸಿ.",
                "Choose one repair category based on local demand.": "ಸ್ಥಳೀಯ ಬೇಡಿಕೆಯ ಆಧಾರದ ಮೇಲೆ ಒಂದು ದುರಸ್ತಿ ವಿಭಾಗವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ.",
                "Keep commonly required spare parts.": "ಸಾಮಾನ್ಯವಾಗಿ ಅಗತ್ಯವಿರುವ ಸ್ಪೇರ್ ಪಾರ್ಟ್ಸ್‌ಗಳನ್ನು ಇಟ್ಟುಕೊಳ್ಳಿ.",
                "Build trust through transparent pricing and service records.": "ಪಾರದರ್ಶಕ ಬೆಲೆ ಮತ್ತು ಸೇವಾ ದಾಖಲೆಗಳ ಮೂಲಕ ವಿಶ್ವಾಸವನ್ನು ನಿರ್ಮಿಸಿ."
            }
        }
    }

    def business_content(kind, value):
        return BUSINESS_CONTENT_TR.get(language, {}).get(kind, {}).get(value, value)

    # Names shown in the recommendation cards.
    BUSINESS_NAME_TR = {
        "Hindi": {
            "Vegetable Cultivation":"सब्ज़ी की खेती",
            "Small Food Processing Unit":"छोटी खाद्य प्रसंस्करण इकाई",
            "Grocery & Daily-Needs Store":"किराना और दैनिक जरूरतों की दुकान",
            "Street Food / Snack Business":"स्ट्रीट फूड / स्नैक व्यवसाय",
            "Dairy / Milk-Based Business":"डेयरी / दूध आधारित व्यवसाय",
            "Goat / Sheep Rearing":"बकरी / भेड़ पालन",
            "Poultry Farming":"पोल्ट्री फार्मिंग",
            "Local Delivery & Transport Service":"स्थानीय डिलीवरी और परिवहन सेवा",
            "Tailoring & Garment Service":"सिलाई और परिधान सेवा",
            "Handicrafts & Local Products":"हस्तशिल्प और स्थानीय उत्पाद",
            "Farm Input & Agri Service Centre":"कृषि इनपुट और कृषि सेवा केंद्र",
            "Small Repair & Service Centre":"छोटा मरम्मत और सेवा केंद्र"
        },
        "Kannada": {
            "Vegetable Cultivation":"ತರಕಾರಿ ಕೃಷಿ",
            "Small Food Processing Unit":"ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಘಟಕ",
            "Grocery & Daily-Needs Store":"ಕಿರಾಣಿ ಮತ್ತು ದೈನಂದಿನ ಅಗತ್ಯಗಳ ಅಂಗಡಿ",
            "Street Food / Snack Business":"ಸ್ಟ್ರೀಟ್ ಫುಡ್ / ತಿಂಡಿ ವ್ಯವಹಾರ",
            "Dairy / Milk-Based Business":"ಡೈರಿ / ಹಾಲು ಆಧಾರಿತ ವ್ಯವಹಾರ",
            "Goat / Sheep Rearing":"ಮೇಕೆ / ಕುರಿ ಸಾಕಣೆ",
            "Poultry Farming":"ಕೋಳಿ ಸಾಕಣೆ",
            "Local Delivery & Transport Service":"ಸ್ಥಳೀಯ ವಿತರಣೆ ಮತ್ತು ಸಾರಿಗೆ ಸೇವೆ",
            "Tailoring & Garment Service":"ಹೊಲಿಗೆ ಮತ್ತು ಉಡುಪು ಸೇವೆ",
            "Handicrafts & Local Products":"ಕರಕುಶಲ ಮತ್ತು ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳು",
            "Farm Input & Agri Service Centre":"ಕೃಷಿ ಇನ್‌ಪುಟ್ ಮತ್ತು ಕೃಷಿ ಸೇವಾ ಕೇಂದ್ರ",
            "Small Repair & Service Centre":"ಸಣ್ಣ ದುರಸ್ತಿ ಮತ್ತು ಸೇವಾ ಕೇಂದ್ರ"
        }
    }

    REASON_TR = {
        "Hindi": {
            "Your available capital comfortably covers the indicative investment range.":"आपकी उपलब्ध पूंजी अनुमानित निवेश सीमा को आराम से कवर करती है।",
            "Your capital fits the lower-to-middle part of the indicative investment range.":"आपकी पूंजी अनुमानित निवेश सीमा के शुरुआती से मध्य भाग में फिट होती है।",
            "Your capital is below the typical starting range, so a smaller pilot may be needed.":"आपकी पूंजी सामान्य शुरुआती सीमा से कम है, इसलिए छोटा पायलट बेहतर हो सकता है।",
            "Capital is currently limited for this model.":"इस मॉडल के लिए वर्तमान पूंजी सीमित है।",
            "Your available resources can support this type of business.":"आपके उपलब्ध संसाधन इस प्रकार के व्यवसाय में मदद कर सकते हैं।",
            "You may need to arrange some additional resources before starting.":"शुरू करने से पहले आपको कुछ अतिरिक्त संसाधनों की व्यवस्था करनी पड़ सकती है।",
            "The business matches your stated interest.":"यह व्यवसाय आपकी बताई गई रुचि से मेल खाता है।",
            "Good water availability improves feasibility.":"अच्छी पानी की उपलब्धता व्यवहार्यता बढ़ाती है।",
            "Limited water availability makes this business more sensitive to planning.":"सीमित पानी की उपलब्धता के कारण इस व्यवसाय में बेहतर योजना की जरूरत है।",
            "Your existing experience reduces the learning curve.":"आपका अनुभव सीखने की अवधि को कम करता है।",
            "Your experience is a strong fit for execution.":"आपका अनुभव इस व्यवसाय को चलाने के लिए उपयोगी है।",
            "A small pilot and basic training are recommended before scaling.":"बड़ा निवेश करने से पहले छोटा पायलट और बुनियादी प्रशिक्षण उपयोगी रहेगा।"
        },
        "Kannada": {
            "Your available capital comfortably covers the indicative investment range.":"ನಿಮ್ಮ ಲಭ್ಯವಿರುವ ಬಂಡವಾಳವು ಅಂದಾಜು ಹೂಡಿಕೆ ವ್ಯಾಪ್ತಿಯನ್ನು ಸುಲಭವಾಗಿ ಪೂರೈಸುತ್ತದೆ.",
            "Your capital fits the lower-to-middle part of the indicative investment range.":"ನಿಮ್ಮ ಬಂಡವಾಳವು ಅಂದಾಜು ಹೂಡಿಕೆ ವ್ಯಾಪ್ತಿಯ ಆರಂಭಿಕದಿಂದ ಮಧ್ಯಮ ಭಾಗಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "Your capital is below the typical starting range, so a smaller pilot may be needed.":"ನಿಮ್ಮ ಬಂಡವಾಳವು ಸಾಮಾನ್ಯ ಆರಂಭಿಕ ವ್ಯಾಪ್ತಿಗಿಂತ ಕಡಿಮೆಯಿದೆ; ಆದ್ದರಿಂದ ಸಣ್ಣ ಪೈಲಟ್ ಸೂಕ್ತವಾಗಬಹುದು.",
            "Capital is currently limited for this model.":"ಈ ಮಾದರಿಗೆ ಪ್ರಸ್ತುತ ಬಂಡವಾಳ ಸೀಮಿತವಾಗಿದೆ.",
            "Your available resources can support this type of business.":"ನಿಮ್ಮ ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳು ಈ ರೀತಿಯ ವ್ಯವಹಾರಕ್ಕೆ ಸಹಾಯ ಮಾಡಬಹುದು.",
            "You may need to arrange some additional resources before starting.":"ಆರಂಭಿಸುವ ಮೊದಲು ಕೆಲವು ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳನ್ನು ವ್ಯವಸ್ಥೆ ಮಾಡಬೇಕಾಗಬಹುದು.",
            "The business matches your stated interest.":"ಈ ವ್ಯವಹಾರವು ನಿಮ್ಮ ಆಸಕ್ತಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "Good water availability improves feasibility.":"ಉತ್ತಮ ನೀರಿನ ಲಭ್ಯತೆ ವ್ಯವಹಾರದ ಸಾಧ್ಯತೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.",
            "Limited water availability makes this business more sensitive to planning.":"ಸೀಮಿತ ನೀರಿನ ಲಭ್ಯತೆಯಿಂದ ಉತ್ತಮ ಯೋಜನೆ ಅಗತ್ಯವಾಗುತ್ತದೆ.",
            "Your existing experience reduces the learning curve.":"ನಿಮ್ಮ ಅನುಭವ ಕಲಿಕೆಯ ಅವಧಿಯನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.",
            "Your experience is a strong fit for execution.":"ನಿಮ್ಮ ಅನುಭವ ವ್ಯವಹಾರ ನಡೆಸಲು ಉತ್ತಮವಾಗಿ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.",
            "A small pilot and basic training are recommended before scaling.":"ವಿಸ್ತರಿಸುವ ಮೊದಲು ಸಣ್ಣ ಪೈಲಟ್ ಮತ್ತು ಮೂಲಭೂತ ತರಬೇತಿ ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ."
        }
    }

    def business_name(value):
        return BUSINESS_NAME_TR.get(language, {}).get(value, value)

    def reason_text(value):
        return REASON_TR.get(language, {}).get(value, value)

    BUSINESS_SCHEME_NAME_TR = {
        "Hindi": {
            "Kisan Credit Card": "किसान क्रेडिट कार्ड",
            "PMEGP": "PMEGP – प्रधानमंत्री रोजगार सृजन कार्यक्रम",
            "MUDRA": "प्रधानमंत्री मुद्रा योजना (MUDRA)",
            "PM SVANidhi": "PM SVANidhi – प्रधानमंत्री स्ट्रीट वेंडर्स आत्मनिर्भर निधि",
            "PMFME": "PMFME – प्रधानमंत्री सूक्ष्म खाद्य प्रसंस्करण उद्यम योजना",
            "Agriculture Infrastructure Fund": "कृषि अवसंरचना कोष",
            "ACABC": "एग्री-क्लिनिक और एग्री-बिजनेस सेंटर (ACABC)",
            "PM Vishwakarma": "PM विश्वकर्मा"
        },
        "Kannada": {
            "Kisan Credit Card": "ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್",
            "PMEGP": "PMEGP – ಪ್ರಧಾನ ಮಂತ್ರಿ ಉದ್ಯೋಗ ಸೃಜನ ಕಾರ್ಯಕ್ರಮ",
            "MUDRA": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಮುದ್ರಾ ಯೋಜನೆ (MUDRA)",
            "PM SVANidhi": "PM SVANidhi – ಪ್ರಧಾನ ಮಂತ್ರಿ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳ ಆತ್ಮನಿರ್ಭರ ನಿಧಿ",
            "PMFME": "PMFME – ಪ್ರಧಾನ ಮಂತ್ರಿ ಸೂಕ್ಷ್ಮ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮ ಯೋಜನೆ",
            "Agriculture Infrastructure Fund": "ಕೃಷಿ ಮೂಲಸೌಕರ್ಯ ನಿಧಿ",
            "ACABC": "ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳು (ACABC)",
            "PM Vishwakarma": "PM ವಿಶ್ವಕರ್ಮ"
        }
    }

    def business_scheme_name(value):
        return BUSINESS_SCHEME_NAME_TR.get(language, {}).get(value, value)

    if st.button(tr("generate"), type="primary", use_container_width=True):
        scored = []

        # All five user inputs are now guaranteed to exist.
        for business in BUSINESSES:
            score, reasons = calculate_match(
                business=business,
                capital=capital,
                resource=resource,
                interest=interest,
                water=water,
                experience=experience,
                location=location
            )
            scored.append({
                "business": business,
                "score": score,
                "reasons": reasons
            })

        scored.sort(key=lambda x: x["score"], reverse=True)
        top = scored[:3]

        st.success(tr("three"))

        for rank, item in enumerate(top, start=1):
            business = item["business"]
            score = item["score"]
            display_name = business_name(business["name"])

            st.markdown(
                f"""
                <div class="recommendation">
                    <h2>#{rank} {display_name}</h2>
                    <div class="score">{score}% {tr("match")}</div>
                    <p><strong>{tr("investment")}:</strong> {business_content("investment", business["investment"])}</p>
                    <p><strong>{tr("model")}:</strong> {business_content("model", business["model"])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            left, right = st.columns(2)
            with left:
                st.markdown("#### " + tr("why_match"))
                for reason in item["reasons"][:4]:
                    st.write("✅ " + reason_text(reason))
                st.markdown("#### " + tr("risk"))
                st.write("⚠️ " + business_content("risk", business["risk"]))

            with right:
                st.markdown("#### " + tr("steps"))
                for step in business["steps"]:
                    st.write("• " + business_content("steps", step))
                st.markdown("#### " + tr("relevant"))
                for scheme in business["schemes"]:
                    st.write("🏛️ " + business_scheme_name(scheme))

            st.divider()

        st.markdown(f"### {tr('next_action')}")
        best = top[0]["business"]
        if capital < best["capital"][0]:
            st.warning(tr("below", business=business_name(best["name"])))
        else:
            st.success(tr("next", business=business_name(best["name"])))

        st.caption(tr("limit"))

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    f"""
    <div class="footer">
        {tr("footer")}<br>
        <span class="small-note">{tr("footer_note")}</span>
    </div>
    """,
    unsafe_allow_html=True
)
