from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line_words, width, is_last_line):
            if is_last_line or len(line_words) == 1:
                return ' '.join(line_words).ljust(width)
            total_chars = sum(len(word) for word in line_words)
            total_spaces = width - total_chars
            num_gaps = len(line_words) - 1
            even_spaces = total_spaces // num_gaps
            extra_spaces = total_spaces % num_gaps
            line = ''
            for i in range(num_gaps):
                line += line_words[i]
                spaces = even_spaces + (1 if i < extra_spaces else 0)
                line += ' ' * spaces
            line += line_words[-1]  
            return line
        result = []
        current_line = []
        current_length = 0
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                result.append(justify_line(current_line, maxWidth, False))
                current_line = []
                current_length = 0
            current_line.append(word)
            current_length += len(word)
        if current_line:
            result.append(justify_line(current_line, maxWidth, True))
        return result
solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
