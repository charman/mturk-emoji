mturk-emoji
===========

Python + JavaScript workaround for mturk's rejection of Emoji

As of early 2018, Amazon's Mechanical Turk service rejects CSV HIT
files that contain 4-byte UTF-8 characters - such as Emoji.

This repository contains Python code in
[encode_emoji.py](encode_emojiy.py) for converting all 4-byte UTF-8
characters into HTML spans with the 4 bytes stored as JSON data.
Sample usage:

``` python
>>> import codecs
>>> from encode_emoji import replace_emoji_characters
>>> grin_emoji = codecs.open('grin_emoji.txt', encoding='utf-8').read().strip()
>>> replace_emoji_characters(grin_emoji)
u"<span class='emoji-bytes' data-emoji-bytes='[240, 159, 152, 128]'></span>"
>>> 
```

The repository also contains JavaScript code in
[decode_emoji.js](decode_emoji.js) that finds all HTML spans created
by [encode_emoji.py](encode_emoji.py) and inserts the Emoji character
into the span, so that this tag:

``` html
<span class='emoji-bytes' data-emoji-bytes='[240, 159, 152, 128]'></span>
```

is replaced with:

``` html
<span class='emoji-bytes' data-emoji-bytes='[240, 159, 152, 128]'>😀</span>
```

which is just rendered as the original Emoji:

``` html
😀
```

Sample usage:

``` html
<script src="https://code.jquery.com/jquery-3.3.1.js"
        integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous"></script>
<script src="decode_emoji.js"></script>

<script>
$(document).ready(function() {
  $('span.emoji-bytes').each(displayEmoji);
});
</script>
```
