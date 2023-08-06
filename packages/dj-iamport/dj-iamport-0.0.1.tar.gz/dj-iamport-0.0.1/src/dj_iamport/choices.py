from django.db.models import TextChoices, IntegerChoices


class IamportPaymentMethodChoices(TextChoices):
    samsung = "samsung", "삼성페이"
    card = "card", "신용카드"
    trans = "trans", "계좌이체"
    vbank = "vbank", "가상계좌"
    phone = "phone", "휴대폰"
    cultureland = "cultureland", "문화상품권"
    smartculture = "smartculture", "스마트문상"
    booknlife = "booknlife", "도서문화상품권"
    happymoney = "happymoney", "해피머니"
    point = "point", "포인트"
    ssgpay = "ssgpay", "SSGPAY"
    lpay = "lpay", "LPAY"
    payco = "payco", "페이코"
    kakaopay = "kakaopay", "카카오페이"
    tosspay = "tosspay", "토스"
    naverpay = "naverpay", "네이버페이"


class IamportPaymentChannelChoices(TextChoices):
    PC = "pc", "PC결제"
    MOBILE = "mobile", "모바일결제"
    API = "api", "API결제"


class IamportPaymentPgProviderChoices(TextChoices):
    INICIS = "inicis", "이니시스"
    NICE = "nice", "나이스정보통신"


class IamportPaymentEmbPgProviderChoices(TextChoices):
    CHAI = "chai", "차이"
    KAKAOPAY = "kakaopay", "카카오페이"


class IamportPaymentCardCodeChoices(TextChoices):
    BC = "361", "BC카드"
    KJ = "364", "광주카드"
    SAMSUNG = "365", "삼성카드"
    SHINHAN = "366", "신한카드"
    HYUNDAI = "367", "현대카드"
    LOTTE = "368", "롯데카드"
    SH = "369", "수협카드"
    CITY = "370", "씨티카드"
    NH = "371", "NH카드"
    JB = "372", "전북카드"
    JEJU = "373", "제주카드"
    HANA = "374", "하나SK카드"
    KB = "381", "KB국민카드"
    WOORI = "041", "우리카드"
    POST = "071", "우체국"


class IamportPaymentCardTypeChoices(IntegerChoices):
    CREDIT = 0, "신용카드"
    CHECK = 1, "체크카드"


class IamportPaymentCurrencyChoices(TextChoices):
    KRW = "KRW", "원"
    USD = "USD", "미화달러"
    EUR = "EUR", "유로"


class IamportPaymentStatusChoices(TextChoices):
    READY = "ready", "미결제"
    PAID = "paid", "결제완료"
    CANCELLED = "cancelled", "결제취소"
    FAILED = "failed", "결제실패"


class IamportPaymentCustomerUidUsageChoices(TextChoices):
    null = None, "일반결제"
    issue = "issue", "빌링키 발급"
    payment = "payment", "결제"
    payment.scheduled = "payment.scheduled", "예약결제"
