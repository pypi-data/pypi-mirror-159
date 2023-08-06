import logging

import requests
from django.db import models
from django.utils.translation import gettext_lazy as _

from findmydevice.models.base import FmdBaseModel


logger = logging.getLogger(__name__)


class Device(FmdBaseModel):
    """
    In FMD project it's named "user"
    """

    name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_('Optional Name for this Device. e.g.: Username ;) Just displayed in the admin'),
    )
    hashed_password = models.CharField(max_length=64, editable=False)
    privkey = models.CharField(max_length=2048, unique=True, editable=False)
    pubkey = models.CharField(max_length=512, unique=True, editable=False)
    push_url = models.URLField(
        help_text=_('Push notification URL (Set by FMD app)'), blank=True, null=True
    )
    command2user = models.CharField(max_length=128, blank=True, null=True, editable=False)
    # pictures=

    def push_notification(self, text):
        if not self.push_url:
            logger.error('No push URL registered for %s', self)
        else:
            data = text.encode(encoding='utf-8')
            requests.post(self.push_url, data=data)

    def __str__(self):
        if self.name:
            return self.name
        return f'>no name< ({self.uuid})'
