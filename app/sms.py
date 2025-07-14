
from app.adapters.sms.afrosms_adapter import AfroSMSAdapter

from app.config import settings


def get_sms_adapter():
    sms_adapter = AfroSMSAdapter(
        identifier_id=settings.AFROSMS_IDENTIFIER_URL,
        auth_token=settings.AFROSMS_TOKEN
    )

    return sms_adapter