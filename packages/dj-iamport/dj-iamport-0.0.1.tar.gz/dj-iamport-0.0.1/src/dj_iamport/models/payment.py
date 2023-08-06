from django.db import models

from dj_iamport.choices import *


class IamportPaymentManager(models.Manager):
    pass


class IamportPayment(models.Model):
    imp_uid = models.CharField("아임포트 결제 고유 UID", max_length=500)
    merchant_uid = models.CharField("가맹점에서 전달한 거래 고유 UID", max_length=500)
    pay_method = models.CharField("결제방법", choices=IamportPaymentMethodChoices.choices, blank=True, max_length=500)
    channel = models.CharField(
        "결제가 발생된 경로",
        choices=IamportPaymentChannelChoices.choices,
        blank=True,
        max_length=500,
    )
    pg_provider = models.CharField("PG사 명칭", IamportPaymentPgProviderChoices.choices, blank=True, max_length=500)
    emb_pg_provider = models.CharField("허브형결제 PG사 명칭", blank=True, max_length=500)
    pg_tid = models.CharField("PG사 승인정보", blank=True, null=True, max_length=500)
    pg_id = models.CharField("거래가 처리된 PG사 상점아이디", blank=True, null=True, max_length=500)
    escrow = models.BooleanField("에스크로결제 여부", blank=True, null=True)
    apply_num = models.CharField("카드사 승인정보", help_text="계좌이체/가상계좌는 값 없음", blank=True, max_length=500)
    bank_code = models.CharField("은행 표준코드", help_text="금융결제원기준", blank=True, max_length=500)
    bank_name = models.CharField("은행 명칭", help_text="실시간계좌이체 결제 건의 경우", blank=True, max_length=500)
    card_code = models.CharField("카드사 코드번호", help_text="금융결제원 표준코드번호", blank=True, max_length=500)
    card_name = models.CharField("카드사 명칭", help_text="신용카드 결제 건의 경우", blank=True, max_length=500)
    card_quota = models.IntegerField("할부개월 수", help_text="0이면 일시불", blank=True, null=True)
    card_number = models.CharField(
        "결제에 사용된 마스킹된 카드번호",
        help_text="7~12번째 자리를 마스킹하는 것이 일반적이지만, PG사의 정책/설정에 따라 다소 차이가 있을 수 있음",
        blank=True,
        max_length=500,
    )
    card_type = models.IntegerField(
        "카드유형",
        choices=IamportPaymentCardTypeChoices.choices,
        help_text="해당 정보를 제공하지 않는 일부 PG사의 경우 null로 응답(ex. JTNet, 이니시스-빌링)",
        blank=True,
        null=True,
    )
    vbank_code = models.CharField("가상계좌 은행 표준코드", help_text="금융결제원기준", blank=True, max_length=500)
    vbank_name = models.CharField("입금받을 가상계좌 은행명", blank=True, max_length=500)
    vbank_num = models.CharField("입금받을 가상계좌 계좌번호", blank=True, max_length=500)
    vbank_holder = models.CharField("입금받을 가상계좌 예금주", blank=True, max_length=500)
    vbank_date = models.IntegerField("입금받을 가상계좌 마감기한", help_text="UNIX timestamp", blank=True, null=True)
    vbank_issued_at = models.IntegerField("가상계좌 생성 시각", help_text="UNIX timestamp", blank=True, null=True)
    name = models.CharField("주문명칭", blank=True, max_length=500)
    amount = models.IntegerField("주문(결제)금액", blank=True, null=True)
    cancel_amount = models.IntegerField("결제취소금액", blank=True, null=True)
    currency = models.CharField(
        "결제승인 화폐단위",
        choices=IamportPaymentCurrencyChoices.choices,
        blank=True,
        max_length=500,
    )
    buyer_name = models.CharField("주문자명", blank=True, max_length=500)
    buyer_email = models.CharField("주문자 Email주소", blank=True, max_length=500)
    buyer_tel = models.CharField("주문자 전화번호", blank=True, max_length=500)
    buyer_addr = models.CharField("주문자 주소", blank=True, max_length=500)
    buyer_postcode = models.CharField("주문자 우편번호", blank=True, max_length=500)
    custom_data = models.CharField("가맹점에서 전달한 custom data", help_text="JSON string 전달", blank=True, max_length=500)
    user_agent = models.CharField("구매자가 결제를 시작한 단말기의 UserAgent 문자열", blank=True, max_length=500)
    status = models.CharField("결제상태", choices=IamportPaymentStatusChoices.choices, blank=True, max_length=500)
    started_at = models.IntegerField(
        "결제시작시점",
        help_text="UNIX timestamp, IMP.request_pay() 를 통해 결제창을 최초 오픈한 시각",
        blank=True,
        null=True,
    )
    paid_at = models.IntegerField("결제완료시점", help_text="UNIX timestamp, 결제완료가 아닐 경우 0", blank=True, null=True)
    failed_at = models.IntegerField("결제실패시점", help_text="UNIX timestamp, 결제실패가 아닐 경우 0", blank=True, null=True)
    cancelled_at = models.IntegerField("결제취소시점", help_text="UNIX timestamp, 결제취소가 아닐 경우 0", blank=True, null=True)
    fail_reason = models.CharField("결제실패 사유", blank=True, max_length=500)
    cancel_reason = models.CharField("결제취소 사유", blank=True, max_length=500)
    receipt_url = models.CharField("신용카드 매출전표 확인 URL", blank=True, max_length=500)
    cash_receipt_issued = models.BooleanField("현금영수증 자동발급 여부", blank=True, null=True)
    customer_uid = models.CharField(help_text="결제창을 통해 빌링키 발급 성공한 결제건의 경우 요청된 customer_uid 값을 응답", blank=True, max_length=500)
    customer_uid_usage = models.CharField(
        "customer_uid가 결제처리에 사용된 상세 용도",
        choices=IamportPaymentCustomerUidUsageChoices.choices,
        blank=True,
        max_length=500,
    )

    """
    cancel_history (Array[PaymentCancelAnnotation], optional): 취소/부분취소 내역 ,
    cancel_receipt_urls (Array[string], optional): (Deprecated : cancel_history 사용 권장) 취소/부분취소 시 생성되는 취소 매출전표 확인 URL. 부분취소 횟수만큼 매출전표가 별도로 생성됨 ,
    """


class IamportPaymentCancel(models.Model):
    payment = models.ForeignKey(
        IamportPayment,
        verbose_name="결제내역",
        on_delete=models.CASCADE,
        related_name="cancel_history_set",
        related_query_name="cancel_history",
    )
    pg_tid = models.CharField("PG사 승인취소번호", max_length=500)
    amount = models.IntegerField("취소 금액")
    cancelled_at = models.IntegerField("결제취소 된 시각", help_text="UNIX timestamp")
    reason = models.CharField("결제취소 사유", max_length=500)
    receipt_url = models.CharField("취소에 대한 매출전표 확인 URL", help_text="PG사에 따라 제공되지 않는 경우도 있음", max_length=500)
