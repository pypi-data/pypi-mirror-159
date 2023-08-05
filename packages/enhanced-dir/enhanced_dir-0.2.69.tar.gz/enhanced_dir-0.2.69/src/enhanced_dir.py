def enhanced_dir(arg, categorize=True, show_types=False, checks=False, interfaces_and_types=False, print_width=120,
                 p=False, show_failed_output=False, show_graphs=False, show_arguments=False, no_of_arguments=2):
    from collections import defaultdict
    if not categorize:
        return_list = []
    passed = defaultdict(lambda: defaultdict(set))
    failed = defaultdict(set)
    passed_ = defaultdict(lambda: defaultdict(set))
    failed_ = defaultdict(lambda: defaultdict(set))
    failed_output = defaultdict(dict)
    x = arg

    for method in (set(dir(arg)) | (set(dir(type(x))) - set(dir(x)))):
        try:
            type_ = type(eval(f'x.{method}'))
        except:
            failed[f'{arg}'].add(method)
            failed_output[f'{arg}'].update()
            continue
        try:
            qualname = eval(f'x.{method}.__qualname__')
            qualname = qualname.split('.')
            passed[f'{arg}'][qualname[0]].add(qualname[1])
            passed_[f'{arg}'][type_].add(qualname[1])
        except:
            failed[f'{arg}'].add(method)
            failed_[f'{arg}'][type_].add(method)
            if show_failed_output:
                output = eval(f'x.{method}')
                failed_output[f'{arg}'].update({method: output})
    if categorize:
        return_list = [{'passed': passed}, {'failed': failed}]
    if show_types:
        return_list.extend(({'passed_types': passed_}, {'failed_types': failed_}))
    if show_failed_output:
        return_list.append({'failed_output': failed_output})
    if interfaces_and_types:
        import collections.abc
        import types
        import typing
        collections_abc = {*()}
        for i in dir(collections.abc):
            try:
                if isinstance(arg, eval(f'collections.abc.{i}')):
                    collections_abc.add(i)
            except:
                pass
        return_list.append({'collections_abc': collections_abc})
        types_ = {*()}
        for i in dir(types):
            try:
                if isinstance(arg, eval(f'types.{i}')):
                    types_.add(i)
            except:
                pass
        return_list.append({'types': types_})
        typing_ = {*()}
        for i in dir(typing):
            try:
                if isinstance(arg, eval(f'typing.{i}')):
                    typing_.add(i)
            except:
                pass
        return_list.append({'typing': typing_})

    if checks:
        checks_ = {}
        try:
            class A(x):
                pass

            checks_['inheritable'] = True
        except:
            checks_['inheritable'] = False

        try:
            a = defaultdict(arg)
            checks_['defaultdict_arg'] = True
        except:
            checks_['defaultdict_arg'] = False

        try:
            d = {arg: 1}
            checks_['dict_key'] = True
        except:
            checks_['dict_key'] = False

        try:
            for i in arg:
                pass
            checks_['iterable'] = True
        except:
            checks_['iterable'] = False
        return_list.append([checks_])

    if show_graphs:
        import matplotlib.pyplot as plt
        import seaborn
        plt.rcParams["figure.figsize"] = (10, 6)
        dc = {i: len(j) for i, j in passed[f'{arg}'].items()}
        dc_1 = {i: len(j) for i, j in {**passed_[f'{arg}'], **failed_[f'{arg}']}.items()}
        data, keys = [dc.values(), dc_1.values()], [dc.keys(), dc_1.keys()]
        fig, axes = plt.subplots(1, 2)
        palette_color = seaborn.color_palette('bright')
        axes[0].pie(data[0], labels=keys[0], colors=palette_color,
                    autopct=lambda p: f'{int(round(p * sum(data[0]) / 100))}')
        axes[1].pie(data[1], labels=keys[1], colors=palette_color,
                    autopct=lambda p: f'{int(round(p * sum(data[1]) / 100))}')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.4)
        plt.show()

    if show_arguments:
        import enhanced_dir
        for i, j in passed[f'{arg}'].items():
            for t in j:
                return_list.append([f"""{arg}.{t}: {enhanced_dir.argument_inspector(f"{arg}.{t}",
                                                                                    no_of_arguments=no_of_arguments,
                                                                                    show_output=False)}"""])

    if p:
        from pprint import pprint
        pprint(return_list, compact=True, width=print_width)
    else:
        return return_list


def two_way(operation, opposite=False, iterators=False, print_width=120, p=False):
    """
    two_way('+')
    two_way('+', opposite=True)
    """
    import warnings
    warnings.filterwarnings("ignore")
    import re, keyword
    from collections import defaultdict, Counter, OrderedDict, namedtuple
    from decimal import Decimal
    from fractions import Fraction
    failed = defaultdict(set)
    succeeded = defaultdict(set)
    invalid = 'StopIteration|StopAsyncIteration|Error|Warning|Exception|Exit|Interrupt|__|ipython|display|execfile' \
              '|dreload|help|license|open|get_ipython|credits|runfile|copyright|breakpoint|input|print'
    bytes_iterator = "(iter(b''))"
    bytearray_iterator = "(iter(bytearray()))"
    dict_keyiterator = "(iter({}.keys()))"
    dict_valueiterator = "(iter({}.values()))"
    dict_itemiterator = "(iter({}.items()))"
    list_iterator = "(iter([]))"
    list_reverseiterator = "(iter(reversed([])))"
    range_iterator = "(iter(range(0)))"
    set_iterator = "(iter(set()))"
    str_iterator = "(iter(''))"
    tuple_iterator = "(iter(()))"
    zip_iterator = "(iter(zip()))"
    line_iterator = "(lambda x: 1).__code__.co_lines"
    positions_iterator = "(lambda x: 1).__code__.co_positions"
    mappingproxy = '(type.__dict__)'
    generator = '((lambda: (yield))())'
    ## views ##
    dict_keys = 'dict().keys'
    dict_values = 'dict().values'
    dict_items = 'dict().items'
    counter = 'Counter'
    ordered_dict = 'OrderedDict'
    default_dict = 'defaultdict'
    named_tuple = 'namedtuple'
    decim = 'Decimal'
    fract = 'Fraction'
    y = [(dict_keys, 13), (dict_values, 14), (dict_items, 15), (mappingproxy, 16),
         (generator, 17), (counter, 18), (ordered_dict, 19), (default_dict, 20), (named_tuple, 21), (decim, 22),
         (fract, 23)]
    if iterators:
        y += [(bytes_iterator, 0), (bytearray_iterator, 1), (dict_keyiterator, 2),
              (dict_valueiterator, 3), (dict_itemiterator, 4), (list_iterator, 5),
              (list_reverseiterator, 6), (range_iterator, 7),
              (set_iterator, 9), (str_iterator, 10), (tuple_iterator, 11), (zip_iterator, 12)]

    for a, i in list(keyword.__builtins__.items()) + y:
        if not re.search(invalid, str(a)):
            for b, j in list(keyword.__builtins__.items()) + y:
                if not re.search(invalid, b):
                    try:
                        x = eval(f'{a}() {operation} {b}()')
                        if opposite:
                            succeeded[f'{b}()'].add(f'{a}()')
                        else:
                            succeeded[f'{a}()'].add(f'{b}()')
                    except:
                        failed[a].add(b)
                    try:
                        x = eval(f'{a}() {operation} {b}')
                        if opposite:
                            succeeded[b].add(f'{a}()')
                        else:
                            succeeded[f'{a}()'].add(b)
                    except:
                        failed[a].add(b)
                    try:
                        x = eval(f'{a} {operation} {b}()')
                        if opposite:
                            succeeded[f'{b}()'].add(a)
                        else:
                            succeeded[a].add(f'{b}()')
                    except:
                        failed[a].add(b)
                    try:
                        x = eval(f'{a} {operation} {b}')
                        if opposite:
                            succeeded[b].add(a)
                        else:
                            succeeded[a].add(b)
                    except:
                        failed[a].add(b)
    if p:
        from pprint import pprint
        pprint([{'succeeded': succeeded}], compact=True, width=print_width)
    else:
        return [{'succeeded': succeeded}]


def operator_check(left_argument, right_argument, show_failed=False, print_width=120, p=False):
    """
    operator_check(1, 2)
    """

    import warnings
    warnings.filterwarnings("ignore")
    failed = set()
    succeeded = set()
    operators = [':', ',', ';', '+', '-', '*', '/', '|', '&', '<', '>', '=',
                 '.', '%', '==', '!=', '<=', '>=', '~', '^', '<<',
                 '>>', '**', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=',
                 '<<=', '>>=', '**=', '//', '//=', '@', '@=', '->', '...',
                 ':=', 'and', 'or', 'in', 'is']

    for operator in operators:
        try:
            x = eval(f'left_argument {operator} right_argument')
            succeeded.add(operator)
        except:
            failed.add(operator)
    returned_dictionary = {'succeeded': succeeded}
    if show_failed:
        returned_dictionary['failed'] = failed
    if p:
        from pprint import pprint
        pprint(returned_dictionary, compact=True, width=print_width)
    else:
        return returned_dictionary


extended_builtins = ['Ellipsis', 'False', 'None', 'NotImplemented', 'True', 'abs', 'all', 'any',
                     'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
                     'classmethod', 'compile', 'complex', 'delattr', 'dict',
                     'dir', 'divmod', 'enumerate', 'eval', 'exec',
                     'filter', 'float', 'frozenset', 'getattr', 'globals', 'hasattr',
                     'hash', 'hex', 'id', 'int', 'isinstance', 'issubclass',
                     'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min',
                     'next', 'object', 'oct', 'ord', 'pow', 'property', 'range',
                     'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
                     'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip',
                     "(iter(b''))", '(iter(bytearray()))', '(iter({}.keys()))',
                     '(iter({}.values()))', '(iter({}.items()))', '(iter([]))',
                     '(iter(reversed([])))', '(iter(range(0)))', '(iter(set()))', "(iter(''))",
                     '(iter(()))', '(iter(zip()))', '(lambda x: 1).__code__.co_lines',
                     '(lambda x: 1).__code__.co_positions', '(type.__dict__)',
                     '((lambda: (yield))())', 'dict().keys', 'dict().values', 'dict().items']

external_checks = {'imports': 'from collections import Counter, namedtuple, defaultdict, OrderedDict, ChainMap, deque;\
                               from types import SimpleNamespace;\
                               from fractions import Fraction;\
                               from decimal import Decimal;',
                   'modules': ['Counter', 'Fraction', 'Decimal', 'defaultdict', 'OrderedDict', 'namedtuple',
                               'SimpleNamespace', 'ChainMap', 'deque']}


def argument_inspector(arg, lib=None, no_of_arguments=2, p=False, print_width=120, show_output=True):
    """
    argument_inspector('int')
    argument_inspector('Fraction', lib='fractions')
    """
    from collections import defaultdict
    import warnings
    warnings.filterwarnings("ignore")
    if show_output:
        rtrnd_dct = defaultdict(dict)
    else:
        rtrnd_dct = defaultdict(set)

    if lib:
        try:
            exec(f'from {lib} import {arg}')
        except:
            pass

    if no_of_arguments >= 0:
        try:
            x = eval(f'{arg}()')
            if show_output:
                rtrnd_dct[0].update({True: x})
            else:
                rtrnd_dct[0].add(True)
        except:
            pass

    if no_of_arguments >= 1:
        import enhanced_dir
        for i in enhanced_dir.extended_builtins + enhanced_dir.inspection_arguments:
            try:
                x = eval(f'{arg}({i})')
                if show_output:
                    rtrnd_dct[1].update({i: x})
                else:
                    rtrnd_dct[1].add(i)
            except:
                pass

            try:
                x = eval(f'{arg}({i}())')
                if show_output:
                    rtrnd_dct[1].update({f'{i}()': x})
                else:
                    rtrnd_dct[1].add(f'{i}()')
            except:
                pass

    if no_of_arguments >= 2:
        for i in enhanced_dir.extended_builtins + enhanced_dir.inspection_arguments:
            for j in enhanced_dir.extended_builtins + enhanced_dir.inspection_arguments:
                try:
                    x = eval(f'{arg}({i}, {j})')
                    if show_output:
                        rtrnd_dct[2].update({(i, j): x})
                    else:
                        rtrnd_dct[2].add((i, j))
                except:
                    pass

                try:
                    x = eval(f'{arg}({i}(), {j}())')
                    if show_output:
                        rtrnd_dct[2].update({(f'{i}()', f'{j}()'): x})
                    else:
                        rtrnd_dct[2].add((f'{i}()', f'{j}()'))
                except:
                    pass

                try:
                    x = eval(f'{arg}({i}(), {j})')
                    if show_output:
                        rtrnd_dct[2].update({(f'{i}()', j): x})
                    else:
                        rtrnd_dct[2].add((f'{i}()', j))
                except:
                    pass

                try:
                    x = eval(f'{arg}({i}, {j}())')
                    if show_output:
                        rtrnd_dct[2].update({(i, f'{j}()'): x})
                    else:
                        rtrnd_dct[2].add((i, f'{j}()'))
                except:
                    pass

                # try:
                #   x = eval(f'{arg}({i!r}, {j!r})')
                #   rtrnd_dct[2].add((i, j))
                # except:
                #   pass

                # try:
                #   x = eval(f'{arg}({i!r}(), {j!r}())')
                #   rtrnd_dct[2].add((f'{i}()', f'{j}()'))
                # except:
                #   pass

                # try:
                #   x = eval(f'{arg}({i!r}(), {j!r})')
                #   rtrnd_dct[2].add((f'{i}()', j))
                # except:
                #   pass

                # try:
                #   x = eval(f'{arg}({i!r}, {j!r}())')
                #   rtrnd_dct[2].add((i, f'{j}()'))
                # except:
                #   pass

    if no_of_arguments >= 3:
        for i in enhanced_dir.extended_builtins + enhanced_dir.inspection_arguments:
            for j in enhanced_dir.extended_builtins + enhanced_dir.inspection_arguments:
                for k in enhanced_dir.extended_builtins + enhanced_dir.inspection_arguments:
                    try:
                        x = eval(f'{arg}({i}, {j}, {k})')
                        if show_output:
                            rtrnd_dct[3].update({(i, j, k): x})
                        else:
                            rtrnd_dct[3].add((i, j, k))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}, {j}, {k}())')
                        if show_output:
                            rtrnd_dct[3].update({(i, j, f'{k}()'): x})
                        else:
                            rtrnd_dct[3].add((i, j, f'{k}()'))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}, {j}(), {k})')
                        if show_output:
                            rtrnd_dct[3].update({(i, f'{j}()', k): x})
                        else:
                            rtrnd_dct[3].add((i, f'{j}()', k))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}, {j}(), {k}())')
                        if show_output:
                            rtrnd_dct[3].update({(i, f'{j}()', f'{k}()'): x})
                        else:
                            rtrnd_dct[3].add((i, f'{j}()', f'{k}()'))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}(), {j}, {k})')
                        if show_output:
                            rtrnd_dct[3].update({(f'{i}()', j, k): x})
                        else:
                            rtrnd_dct[3].add((f'{i}()', j, k))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}(), {j}, {k}())')
                        if show_output:
                            rtrnd_dct[3].update({(f'{i}()', j, f'{k}()'): x})
                        else:
                            rtrnd_dct[3].add((f'{i}()', j, f'{k}()'))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}(), {j}(), {k})')
                        if show_output:
                            rtrnd_dct[3].update({(f'{i}()', f'{j}()', k): x})
                        else:
                            rtrnd_dct[3].add((f'{i}()', f'{j}()', k))
                    except:
                        pass

                    try:
                        x = eval(f'{arg}({i}(), {j}(), {k}())')
                        if show_output:
                            rtrnd_dct[3].update({(f'{i}()', f'{j}()', f'{k}()'): x})
                        else:
                            rtrnd_dct[3].add((f'{i}()', f'{j}()', f'{k}()'))
                    except:
                        pass

    if p:
        from pprint import pprint
        pprint(rtrnd_dct, compact=True, width=print_width)
    else:
        return rtrnd_dct


inspection_arguments = [1, 0, 1.2, 'abc', '1', '0', '1.2', '1/2', {1, 2, 3}, {'a': 1, 'b': 2}, (1, 2, 3),
                        [(2, 5), (3, 2)], [1, 2, 3], [1, 0, 1, 0], {'a', 'b', 'c'}, ('a', 'b', 'c'), ['a', 'b', 'c'],
                        1 + 2j, b'2', b'a', bytearray(1), frozenset({1, 2, 3}), frozenset({'a', 'b', 'c'}),
                        '(lambda x: x < 5)', 'range(2)', "enumerate('a')", '(iter([1, 2, 3]))', '(iter(range(5)))',
                        '(iter(reversed([1, 2, 3])))', '(iter({1, 2, 3}))', "(iter('abc'))", '(iter((1, 2, 3)))',
                        "(iter({'a': 1, 'b': 2}.items()))", "(iter(zip((0, 1, 2), 'abc')))",
                        "(iter({'a': 1, 'b': 2}.keys()))", "(iter({'a': 1, 'b': 2}.values()))",
                        ({'a': 1, 'b': 2}.keys()), ({'a': 1, 'b': 2}.values()), ({'a': 1, 'b': 2}.items()),
                        "(iter(b'2'))", "(iter(b'a'))", '(iter(bytearray(1)))']


def diff2(arg1, arg2, show_graph=0, p=0):
    dir_arg1 = set(dir(arg1))
    dir_arg2 = set(dir(arg2))
    returned_dict = {f'{arg1} - {arg2}': dir_arg1 - dir_arg2,
                     f'{arg2} - {arg1}': dir_arg2 - dir_arg1,
                     f'{arg1} & {arg2}': dir_arg1 & dir_arg2}

    sorted_returned_tuple = sorted(returned_dict.items(), key=lambda x: len(x[1]))
    sorted_returned_list = [{i: j} for i, j in sorted_returned_tuple if j]

    if show_graph:
        import upsetplot
        graph_dict = {f'{arg1}': dir_arg1,
                      f'{arg2}': dir_arg2}

        upset_data_sub = upsetplot.from_contents({k: v for k, v in graph_dict.items()})
        upsetplot.plot(upset_data_sub, show_counts=True, sort_by='cardinality')

    if p:
        from pprint import pprint
        pprint(sorted_returned_list, compact=True, width=120)
    else:
        return sorted_returned_list


def diff3(arg1, arg2, arg3, show_graph=0, p=0):
    returned_dict = {f'{arg1} - {arg2} - {arg3}': set(dir(arg1)) - set(dir(arg2)) - set(dir(arg3)),
                     f'{arg2} - {arg1} - {arg3}': set(dir(arg2)) - set(dir(arg1)) - set(dir(arg3)),
                     f'{arg3} - {arg1} - {arg2}': set(dir(arg3)) - set(dir(arg1)) - set(dir(arg2)),
                     f'{arg1} & {arg2} - {arg3}': set(dir(arg1)) & set(dir(arg2)) - set(dir(arg3)),
                     f'{arg2} & {arg3} - {arg1}': set(dir(arg2)) & set(dir(arg3)) - set(dir(arg1)),
                     f'{arg1} & {arg3} - {arg2}': set(dir(arg1)) & set(dir(arg3)) - set(dir(arg2)),
                     f'{arg1} & {arg2} & {arg3}': set(dir(arg1)) & set(dir(arg2)) & set(dir(arg3))}

    sorted_returned_tuple = sorted(returned_dict.items(), key=lambda x: len(x[1]))
    sorted_returned_list = [{i: j} for i, j in sorted_returned_tuple if j]

    if show_graph:
        import upsetplot
        graph_dict = {f'{arg1}': set(dir(arg1)),
                      f'{arg2}': set(dir(arg2)),
                      f'{arg3}': set(dir(arg3))}

        upset_data_sub = upsetplot.from_contents({k: v for k, v in graph_dict.items()})
        upsetplot.plot(upset_data_sub, show_counts=True, sort_by='cardinality')

    if p:
        from pprint import pprint
        pprint(sorted_returned_list, compact=True, width=120)
    else:
        return sorted_returned_list
