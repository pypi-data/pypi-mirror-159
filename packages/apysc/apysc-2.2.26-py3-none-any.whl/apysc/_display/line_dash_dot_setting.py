"""Dash dot (1-dot chain) setting for a line.
"""

from typing import Union

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class LineDashDotSetting(Dictionary[str, Int]):
    """
    Dash dot (1-dot chain) setting for a line.

    References
    ----------
    - Graphics line_style interface document
        - https://simon-ritchie.github.io/apysc/en/graphics_line_style.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=10)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50)
    >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
    ...     dot_size=2, dash_size=5, space_size=3)
    >>> line.line_dash_dot_setting.dot_size
    Int(2)

    >>> line.line_dash_dot_setting.dash_size
    Int(5)

    >>> line.line_dash_dot_setting.space_size
    Int(3)
    """

    @arg_validation_decos.is_integer(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=2)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=2)
    @arg_validation_decos.is_integer(arg_position_index=3)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
            self, *, dot_size: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> None:
        """
        Dash dot (1-dot chain) setting for a line.

        Parameters
        ----------
        dot_size : int or Int
            Dot size.
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dots and dashes.

        References
        ----------
        - Graphics line_style interface document
            - https://simon-ritchie.github.io/apysc/en/graphics_line_style.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.dot_size
        Int(2)

        >>> line.line_dash_dot_setting.dash_size
        Int(5)

        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        from apysc._converter.to_apysc_val_from_builtin import \
            get_copied_int_from_builtin_val
        dot_size_: Int = get_copied_int_from_builtin_val(
            integer=dot_size)
        dash_size_: Int = get_copied_int_from_builtin_val(
            integer=dash_size)
        space_size_: Int = get_copied_int_from_builtin_val(
            integer=space_size)
        super(LineDashDotSetting, self).__init__({
            'dot_size': dot_size_,
            'dash_size': dash_size_,
            'space_size': space_size_,
        })

    @property
    @add_debug_info_setting(module_name=__name__)
    def dot_size(self) -> Int:
        """
        Get a dot size setting.

        Returns
        -------
        dot_size : Int
            Dot size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.dot_size
        Int(2)
        """
        return self['dot_size']

    @property
    @add_debug_info_setting(module_name=__name__)
    def dash_size(self) -> Int:
        """
        Get a dash size setting.

        Returns
        -------
        dash_size : Int
            Dash size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.dash_size
        Int(5)
        """
        return self['dash_size']

    @property
    @add_debug_info_setting(module_name=__name__)
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Space size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_dash_dot_setting = ap.LineDashDotSetting(
        ...     dot_size=2, dash_size=5, space_size=3)
        >>> line.line_dash_dot_setting.space_size
        Int(3)
        """
        return self['space_size']
