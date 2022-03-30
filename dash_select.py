import dash
from dash import Dash, dcc, html, Input, Output, State, callback_context, no_update

init_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

app = dash.Dash(__name__)
box_style = dict(border='1px solid', margin='15px', padding='10px')
app.layout = html.Div(id='wrapper', children=[
    html.P(id='selection-container', children=init_text, style=box_style),
    # html.P(id='highlight-container', children=init_text, style=box_style),
    dcc.Input(id='selection-text', value='', style=dict(display='none')),
    dcc.Input(id='selection-start', value='', style=dict(display='none')),
    dcc.Input(id='selection-end', value='', style=dict(display='none')),
    dcc.Input(id='raw_text2', value='', style=dict(display='none')),
    dcc.Input(id='raw_text', value='', style=dict(display='none')),
    
    html.Button(id='submit', children='Submit selection'),
    html.P(id='callback-result', children=''),
])


@app.callback(
    Output('callback-result', 'children'),
    # dash.dependencies.Output('highlight-container', 'children'),
    # Output('selection-container', 'children'),
    [
        Input('submit', 'n_clicks'),
        # Input('raw_text2', 'value'),
    ],
    [
        State('raw_text', 'value'),
        State('selection-text', 'value'),
        State('selection-start', 'value'),
        State('selection-end', 'value'),
    ],
        )
def update_output(n_clicks, raw_text, res_text, start, end):
    if res_text:
        startint = int(start)
        endint = int(end)
        before = raw_text[0:startint]
        highlight = html.Mark(raw_text[startint:endint])
        # highlight = html.Span(raw_text[startint:endint])

        # highlight = raw_text[startint:endint]
        after = raw_text[endint:len(raw_text)]
        highlight_text = [before, highlight, after]
        print(highlight_text)
        return res_text #, highlight_text
        # return html.Mark(html.Span(f'Selected string: "{text}"', style=dict(color='green')))
    return html.Span('Nothing selected', style=dict(color='red'))# , no_update


# @app.callback(
#     dash.dependencies.Output('highlight-container', 'children'),
#     dash.dependencies.Input('raw_text2', 'value'),
#         )
# def clear_text(raw_text2):
#     return raw_text2

if __name__ == '__main__':
    app.run_server(debug=True)