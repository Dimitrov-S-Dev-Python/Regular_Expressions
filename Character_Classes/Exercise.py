# Write your regular expressions inside the raw string, for example: r'a+'

# Exercise 14: Match two or more o’s, but only if they’re in the
# middle of a word.
# Do not include any characters other than the o’s in the match
middle_oo_regex = r'\Bo{2,}\B'

# Exercise 15: Match list item strings that start with one or more digits
# followed by a ) -- that is, a closed parenthesis
# Match the entire contents of each list item string (not just the
# digit(s) and parenthesis).
#
# 1) Finish regex course
#    should match the entire string
#
# 223513) Go to bed
#    should match the entire string
#
# I think it would be best to 1) stop, 2) drop, and 3) roll
#    should NOT match
#
# 1. Wake up at noon
#    should NOT match
#
# a) You don't talk about fight club
#    should NOT match
list_item_regex = r'^\d+\).*$'

# Exercise 16: Match any whitespace at the end of a string
# Do not include characters other than the whitespace in the match
# Do not match strings that don’t have whitespace at the end
trailing_whitespace_regex = r''

# Exercise 17: Find any phrase that matches ____ the ____
# That is, one word before and after "the" (without quotes).
# Don't match any non-word characters before or after the matched
# string.
blank_the_blank_regex = r''

# Exercise 18: Make a simplified email address matcher with these rules:
# - One or more word or period (.) characters before the @
# - At least one  period (.) after the @
# - The string should contain only the email address and no
#   surrounding characters
#
# Interested in unsimplified? See http://emailregex.com/
email_regex = r''
