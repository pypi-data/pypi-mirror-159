import pytest

from arrow import arrow, locales


@pytest.mark.usefixtures("lang_locales")
class TestLocaleValidation:
    """Validate locales to ensure that translations are valid and complete"""

    def test_locale_validation(self):

        for locale_cls in self.locales.values():
            # 7 days + 1 spacer to allow for 1-indexing of months
            assert len(locale_cls.day_names) == 8
            assert locale_cls.day_names[0] == ""
            # ensure that all string from index 1 onward are valid (not blank or None)
            assert all(locale_cls.day_names[1:])

            assert len(locale_cls.day_abbreviations) == 8
            assert locale_cls.day_abbreviations[0] == ""
            assert all(locale_cls.day_abbreviations[1:])

            # 12 months + 1 spacer to allow for 1-indexing of months
            assert len(locale_cls.month_names) == 13
            assert locale_cls.month_names[0] == ""
            assert all(locale_cls.month_names[1:])

            assert len(locale_cls.month_abbreviations) == 13
            assert locale_cls.month_abbreviations[0] == ""
            assert all(locale_cls.month_abbreviations[1:])

            assert len(locale_cls.names) > 0
            assert locale_cls.past is not None
            assert locale_cls.future is not None

    def test_locale_name_validation(self):

        for locale_cls in self.locales.values():
            for locale_name in locale_cls.names:
                assert len(locale_name) == 2 or len(locale_name) == 5
                assert locale_name.islower()
                # Not a two-letter code
                if len(locale_name) > 2:
                    assert "-" in locale_name
                    assert locale_name.count("-") == 1

    def test_duplicated_locale_name(self):
        with pytest.raises(LookupError):

            class Locale1(locales.Locale):
                names = ["en-us"]


class TestModule:
    def test_get_locale(self, mocker):
        mock_locale = mocker.Mock()
        mock_locale_cls = mocker.Mock()
        mock_locale_cls.return_value = mock_locale

        with pytest.raises(ValueError):
            arrow.locales.get_locale("locale-name")

        cls_dict = arrow.locales._locale_map
        mocker.patch.dict(cls_dict, {"locale-name": mock_locale_cls})

        result = arrow.locales.get_locale("locale_name")
        assert result == mock_locale

        # Capitalization and hyphenation should still yield the same locale
        result = arrow.locales.get_locale("locale-name")
        assert result == mock_locale

        result = arrow.locales.get_locale("locale-NAME")
        assert result == mock_locale

    def test_get_locale_by_class_name(self, mocker):
        mock_locale_cls = mocker.Mock()
        mock_locale_obj = mock_locale_cls.return_value = mocker.Mock()

        globals_fn = mocker.Mock()
        globals_fn.return_value = {"NonExistentLocale": mock_locale_cls}

        with pytest.raises(ValueError):
            arrow.locales.get_locale_by_class_name("NonExistentLocale")

        mocker.patch.object(locales, "globals", globals_fn)
        result = arrow.locales.get_locale_by_class_name("NonExistentLocale")

        mock_locale_cls.assert_called_once_with()
        assert result == mock_locale_obj

    def test_locales(self):

        assert len(locales._locale_map) > 0


class TestCustomLocale:
    def test_custom_locale_subclass(self):
        class CustomLocale1(locales.Locale):
            names = ["foo", "foo-BAR"]

        assert locales.get_locale("foo") is not None
        assert locales.get_locale("foo-BAR") is not None
        assert locales.get_locale("foo_bar") is not None

        class CustomLocale2(locales.Locale):
            names = ["underscores_ok"]

        assert locales.get_locale("underscores_ok") is not None


@pytest.mark.usefixtures("lang_locale")
class TestEnglishLocale:
    def test_describe(self):
        assert self.locale.describe("now", only_distance=True) == "instantly"
        assert self.locale.describe("now", only_distance=False) == "just now"

    def test_format_timeframe(self):

        assert self.locale._format_timeframe("hours", 2) == "2 hours"
        assert self.locale._format_timeframe("hour", 0) == "an hour"

    def test_format_relative_now(self):

        result = self.locale._format_relative("just now", "now", 0)

        assert result == "just now"

    def test_format_relative_past(self):

        result = self.locale._format_relative("an hour", "hour", 1)

        assert result == "in an hour"

    def test_format_relative_future(self):

        result = self.locale._format_relative("an hour", "hour", -1)

        assert result == "an hour ago"

    def test_ordinal_number(self):
        assert self.locale.ordinal_number(0) == "0th"
        assert self.locale.ordinal_number(1) == "1st"
        assert self.locale.ordinal_number(2) == "2nd"
        assert self.locale.ordinal_number(3) == "3rd"
        assert self.locale.ordinal_number(4) == "4th"
        assert self.locale.ordinal_number(10) == "10th"
        assert self.locale.ordinal_number(11) == "11th"
        assert self.locale.ordinal_number(12) == "12th"
        assert self.locale.ordinal_number(13) == "13th"
        assert self.locale.ordinal_number(14) == "14th"
        assert self.locale.ordinal_number(21) == "21st"
        assert self.locale.ordinal_number(22) == "22nd"
        assert self.locale.ordinal_number(23) == "23rd"
        assert self.locale.ordinal_number(24) == "24th"

        assert self.locale.ordinal_number(100) == "100th"
        assert self.locale.ordinal_number(101) == "101st"
        assert self.locale.ordinal_number(102) == "102nd"
        assert self.locale.ordinal_number(103) == "103rd"
        assert self.locale.ordinal_number(104) == "104th"
        assert self.locale.ordinal_number(110) == "110th"
        assert self.locale.ordinal_number(111) == "111th"
        assert self.locale.ordinal_number(112) == "112th"
        assert self.locale.ordinal_number(113) == "113th"
        assert self.locale.ordinal_number(114) == "114th"
        assert self.locale.ordinal_number(121) == "121st"
        assert self.locale.ordinal_number(122) == "122nd"
        assert self.locale.ordinal_number(123) == "123rd"
        assert self.locale.ordinal_number(124) == "124th"

    def test_meridian_invalid_token(self):
        assert self.locale.meridian(7, None) is None
        assert self.locale.meridian(7, "B") is None
        assert self.locale.meridian(7, "NONSENSE") is None

@pytest.mark.usefixtures("lang_locale")
class TestJapaneseLocale:
    def test_format_timeframe(self):
        assert self.locale._format_timeframe("now", 0) == "現在"
        assert self.locale._format_timeframe("second", 1) == "1秒"
        assert self.locale._format_timeframe("seconds", 30) == "30秒"
        assert self.locale._format_timeframe("minute", 1) == "1分"
        assert self.locale._format_timeframe("minutes", 40) == "40分"
        assert self.locale._format_timeframe("hour", 1) == "1時間"
        assert self.locale._format_timeframe("hours", 23) == "23時間"
        assert self.locale._format_timeframe("day", 1) == "1日"
        assert self.locale._format_timeframe("days", 12) == "12日"
        assert self.locale._format_timeframe("week", 1) == "1週間"
        assert self.locale._format_timeframe("weeks", 38) == "38週間"
        assert self.locale._format_timeframe("month", 1) == "1ヶ月"
        assert self.locale._format_timeframe("months", 11) == "11ヶ月"
        assert self.locale._format_timeframe("year", 1) == "1年"
        assert self.locale._format_timeframe("years", 12) == "12年"

