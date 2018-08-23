from commons import separator_len, separator, text_pad


def show_separator() -> None:
    print(separator)


def _get_pads(total_pad_len, pad_char) -> (str, str):
    left_pad_len = total_pad_len // 2
    right_pad_len = total_pad_len - left_pad_len

    left_pad = pad_char * left_pad_len
    right_pad = pad_char * right_pad_len

    return left_pad, right_pad


def show_text(text: str, show_pad: bool = True) -> None:
    text = text if text is not None else ""
    pad_char = text_pad if show_pad else " "

    total_pad_len = (separator_len - len(text)) if text else separator_len
    left_pad, right_pad = _get_pads(total_pad_len, pad_char)

    print(left_pad, end='')
    print(text, end='')
    print(right_pad)


def show_text_with_separator(text: str, show_pad: bool = True) -> None:
    print()
    show_separator()
    show_text(text, show_pad)
    show_separator()
