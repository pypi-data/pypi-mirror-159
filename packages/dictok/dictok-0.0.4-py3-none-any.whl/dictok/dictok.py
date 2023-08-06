import ahocorasick

class DicTok:

    def __init__(self, dic_file, sep=','):
        self.dict = self.import_dict(dic_file, sep)
        self.atm = self.create_atm()

    def import_dict(self, dic_file, sep):
        dic = {}
        with open(dic_file, 'r', encoding='utf8') as f:
            tokens_list = f.read().splitlines()

        for e in tokens_list:
            if not e:
                continue

            ws = e.split(sep)
            if len(ws) > 1:
                dic[ws[0].lower()] = ws[1]
            else:
                dic[ws[0].lower()] = ws[0]

        return dic

    def create_atm(self):
        atm = ahocorasick.Automaton()

        for w in self.dict.keys():
            atm.add_word(w, w)

        atm.make_automaton()
        return atm

    def has_overlap(self, a, b):
        return len(list(set(a) & set(b)))

    def flatten(self, xss):
        return [x for xs in xss for x in xs]

    def remove_single_chars(self, tokens):
        return [e for e in tokens if len(e) > 1]

    def tokenize(self, text, include_unknown = True, include_single_chars = True):
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
                if r[0] != 0 and include_unknown:
                    ranges.append(list(range(r[1] - 1)))
            elif ranges[-1][-1]  + 1 < r[0] and include_unknown:
                ranges.append(list(range(ranges[-1][-1] + 1, r[0])))

            ranges.append(r)

        if include_unknown:
            ranges.append(list(range(ranges[-1][-1] + 1, len(text))))

        ranges = [e for e in ranges if e != []]

        _tokens = []
        for s in ranges:
            token = text[s[0]:s[-1] + 1].strip()
            if token != '' and include_unknown:
                _tokens.append(token.split(' '))
            else:
                _tokens.append([token])

        tokens = self.flatten(_tokens)

        if not include_single_chars:
            tokens = self.remove_single_chars(tokens)

        tokens_cleaned = []
        for t in tokens:
            if t.lower() in self.dict:
                if t.lower() != self.dict[t.lower()].lower():
                    tokens_cleaned.append(self.dict[t.lower()])
                else:
                    tokens_cleaned.append(t)
            else:
                tokens_cleaned.append(t)

        return tokens_cleaned
