import sublime, sublime_plugin, re

class JhFormatterCommand ( sublime_plugin.TextCommand ):

    def run ( self, edit ):
        region = sublime.Region ( 0, self.view.size ( ) )
        str_in = self.view.substr ( region )
        syntax = self.view.settings ( ).get ( 'syntax' )

        # str_out = JhFormatterCommand.remove_whitespace ( str_in )
        # str_out = JhFormatterCommand.add_newlines ( str_out )
        str_out = JhFormatterCommand.space_parens ( str_in )
        str_out = JhFormatterCommand.capitalize_keywords( str_out )

        self.view.erase ( edit, region )
        self.view.insert ( edit, 0, str_out )

    def remove_whitespace ( str_in ):
        regex = re.compile ( r'\s+' )

        return re.sub ( regex, ' ', str_in )

    def add_newlines ( str_in ):
        tokens= [ ';', '{' ]

        for token in tokens:
            str_in = str_in.replace ( token, token + "\n" )

        return str_in

    def space_parens ( str_in ):
        str_out = str_in.replace ( '(', ' ( ' )
        str_out = str_out.replace ( ')', ' ) ' )
        str_out = str_out.replace ( '::', ' :: ' )
        str_out = str_out.replace ( '->', ' -> ' )
        str_out = str_out.replace ( '=', ' = ' )

        regex = re.compile ( r' +' )
        str_out = re.sub ( regex, ' ', str_out )

        return str_out

    def capitalize_keywords ( str_in ):
        str_out = str_in.replace ( 'namespace', 'Namespace' )
        str_out = str_out.replace ( 'interface', 'Interface' )
        str_out = str_out.replace ( 'class', 'Class' )

        return str_out;