from django.utils.translation import gettext_lazy as _
from django.db import models


class LanguageCodes(models.TextChoices):
    """
    Language options with their codes.
    """
    ar = "ar", _("Arabic")
    af = "af", _("Afrikaans")
    ar_dz = "ar-dz", _("Algerian Arabic")
    ast = "ast", _("Asturian")
    az = "az", _("Azerbaijani")
    bg = "bg", _("Bulgarian")
    be = "be", _("Belarusian")
    bn = "bn", _("Bengali")
    br = "br", _("Breton")
    bs = "bs", _("Bosnian")
    ca = "ca", _("Catalan")
    cs = "cs", _("Czech")
    cy = "cy", _("Welsh")
    da = "da", _("Danish")
    de = "de", _("German")
    dsb = "dsb", _("Lower Sorbian")
    el = "el", _("Greek")
    en = "en", _("English")
    en_au = "en-au", _("Australian English")
    en_gb = "en-gb", _("British English")
    eo = "eo", _("Esperanto")
    es = "es", _("Spanish")
    es_ar = "es-ar", _("Argentinian Spanish")
    es_co = "es-co", _("Colombian Spanish")
    es_mx = "es-mx", _("Mexican Spanish")
    es_ni = "es-ni", _("Nicaraguan Spanish")
    es_ve = "es-ve", _("Venezuelan Spanish")
    et = "et", _("Estonian")
    eu = "eu", _("Basque")
    fa = "fa", _("Persian")
    fi = "fi", _("Finnish")
    fr = "fr", _("French")
    fy = "fy", _("Frisian")
    ga = "ga", _("Irish")
    gd = "gd", _("Scottish Gaelic")
    gl = "gl", _("Galician")
    he = "he", _("Hebrew")
    hi = "hi", _("Hindi")
    hr = "hr", _("Croatian")
    hsb = "hsb", _("Upper Sorbian")
    hu = "hu", _("Hungarian")
    hy = "hy", _("Armenian")
    ia = "ia", _("Interlingua")
    id = "id", _("Indonesian")
    ig = "ig", _("Igbo")
    io = "io", _("Ido")
    ice = "is", _("Icelandic")
    it = "it", _("Italian")
    ja = "ja", _("Japanese")
    ka = "ka", _("Georgian")
    kab = "kab", _("Kabyle")
    kk = "kk", _("Kazakh")
    km = "km", _("Khmer")
    kn = "kn", _("Kannada")
    ko = "ko", _("Korean")
    ky = "ky", _("Kyrgyz")
    lb = "lb", _("Luxembourgish")
    lt = "lt", _("Lithuanian")
    lv = "lv", _("Latvian")
    mk = "mk", _("Macedonian")
    ml = "ml", _("Malayalam")
    mn = "mn", _("Mongolian")
    mr = "mr", _("Marathi")
    ms = "ms", _("Malay")
    my = "my", _("Burmese")
    nb = "nb", _("Norwegian Bokmål")
    ne = "ne", _("Nepali")
    nl = "nl", _("Dutch")
    nn = "nn", _("Norwegian Nynorsk")
    os = "os", _("Ossetic")
    pa = "pa", _("Punjabi")
    pl = "pl", _("Polish")
    pt = "pt", _("Portuguese")
    pt_br = "pt-br", _("Brazilian Portuguese")
    ro = "ro", _("Romanian")
    ru = "ru", _("Russian")
    sk = "sk", _("Slovak")
    sl = "sl", _("Slovenian")
    sq = "sq", _("Albanian")
    sr = "sr", _("Serbian")
    sr_latn = "sr-latn", _("Serbian Latin")
    sv = "sv", _("Swedish")
    sw = "sw", _("Swahili")
    ta = "ta", _("Tamil")
    te = "te", _("Telugu")
    tg = "tg", _("Tajik")
    th = "th", _("Thai")
    tk = "tk", _("Turkmen")
    tr = "tr", _("Turkish")
    tt = "tt", _("Tatar")
    udm = "udm", _("Udmurt")
    uk = "uk", _("Ukrainian")
    ur = "ur", _("Urdu")
    uz = "uz", _("Uzbek")
    vi = "vi", _("Vietnamese")
    zh_hans = "zh-hans", _("Simplified Chinese")
    zh_hant = "zh-hant", _("Traditional Chinese")


class Language(models.Model):
    # TODO: Add language code!
    # name = models.CharField(max_length=50, verbose_name=_("Language"))
    code = models.CharField(
        _('Language'),
        max_length=7,
        choices=LanguageCodes.choices,
        default=LanguageCodes.en,
        unique=True,
        blank=False,
        null=False
    )
    flag = models.ImageField(null=True, blank=True, upload_to='images/flags')
    summary = models.CharField(blank=True, max_length=255)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.get_code_display()
