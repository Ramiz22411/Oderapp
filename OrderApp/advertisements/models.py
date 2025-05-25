from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CategoryAds(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описания")
    image = models.ImageField(upload_to="order_image", verbose_name="Картинка")
    condition = models.BooleanField(default=False, verbose_name="Состояние")
    created_at = models.DateTimeField(auto_created=True, verbose_name="дата добавления")
    category = models.ForeignKey(CategoryAds, on_delete=models.CASCADE, verbose_name="Категория", related_name="ads")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="owners",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "объявлении"

    def __str__(self):
        return self.title


class ExchangeProposal(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = ("Pending", "Ожидает")
        ACCEPTED = ("Accepted", "Принята")
        CANCELED = ("Canceled", "Отклонена")

    sender_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Отправитель",
        related_name="r_proposals"
    )
    receiver_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Получатель",
        related_name="s_proposals"
    )
    status = models.CharField(
        max_length=255,
        choices=StatusChoice.choices,
        verbose_name="Статус",
        default=StatusChoice.PENDING
    )
    comment = models.CharField(max_length=255, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_created=True, verbose_name="дата добавления")

    class Meta:
        verbose_name = "Запрос на обмен"
        verbose_name_plural = "Запросы на обмен"

    def __str__(self):
        return self.status
