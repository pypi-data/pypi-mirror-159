import ahocorasick

class DicTok:

    def __init__(self, dic_file, include_unknown = True, single_chars = True):
        self.atm = self.create_atm(dic_file)
        self.single_chars = single_chars
        self.include_unknown = include_unknown

    def create_atm(self, dic_file):
        atm = ahocorasick.Automaton()

        with open(dic_file, 'r', encoding='utf8') as f:
            tokens_list = f.read().splitlines()

        for w in tokens_list:
            if w:
                atm.add_word(w.lower(), w)

        atm.make_automaton()
        return atm

    def has_overlap(self, a, b):
        return len(list(set(a) & set(b)))

    def flatten(self, xss):
        return [x for xs in xss for x in xs]

    def remove_single_chars(self, tokens):
        return [e for e in tokens if len(e) > 1]

    def fix_typos(self, _tokens):

        with open(self.typos_file, 'r', encoding='utf8') as f:
            typos_list = f.read().splitlines()

        _keys = list(map(lambda x: x.split(',')[0].lower(), typos_list))
        tokens = list(map(lambda x: typos_list[_keys.index(x.lower())].split(',')[1] if x.lower() in _keys else x, _tokens))

        return tokens

    def tokenize(self, text):
        text = str(text)
        mts = {}

        for i, (end, val) in enumerate(self.atm.iter(text.lower())):
            idx = i + 1
            e = end + 1
            start = e - len(val)
            xs = range(start, e)

            overlaps = set()
            for k in mts.keys():
                if self.has_overlap(xs, mts[k][0]):
                    overlaps.add(k)
                    mts[k][1].add(idx)
            mts[idx] = (xs, overlaps, val)

        selected_ids = set()
        for k in mts.keys():
            score_max = len(mts[k][0]) + 1
            selected_index = k
            for j in mts[k][1]:
                score_j = len(mts[j][0]) + 1
                if score_j > score_max:
                    score_max = score_j
                    selected_index = j
            selected_ids.add(selected_index)

        ranges = []
        for i in selected_ids:
            r = list(mts[i][0])
            if ranges == []:
                if r[0] != 0 and self.include_unknown:
                    ranges.append(list(range(r[1] - 1)))
            elif ranges[-1][-1]  + 1 < r[0] and self.include_unknown:
                ranges.append(list(range(ranges[-1][-1] + 1, r[0])))

            ranges.append(r)

        if self.include_unknown:
            ranges.append(list(range(ranges[-1][-1] + 1, len(text))))

        ranges = [e for e in ranges if e != []]

        _tokens = []
        for s in ranges:
            token = text[s[0]:s[-1] + 1].strip()
            if token != '' and self.include_unknown:
                _tokens.append(token.split(' '))
            else:
                _tokens.append([token])

        tokens = self.flatten(_tokens)

        if not self.single_chars:
            tokens = self.remove_single_chars(tokens)

        return tokens
