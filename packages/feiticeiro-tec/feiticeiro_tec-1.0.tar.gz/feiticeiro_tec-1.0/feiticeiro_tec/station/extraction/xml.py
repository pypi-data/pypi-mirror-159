def xml_get_column(text: str,column:str, after=[]):
    """Pega o text De Uma String Com Estrutura De XML

    text = "
    <ColumnaA>
        <ColumnaB>
            <ColumnaA> Aqui </ColumnaA>
        </ColumnaB>
    </ColumnaA>
    column = 'Numero'
    after = ['<ColumnaB>','<ColumnaA>']

    """
    try:
        for after in after:
            if text.find(start) == -1:
                return False
            text = text[text.find(after)+len(after):]
        start = f'<{column}>'
        end = f'</{column}>'
        if text.find(start) == -1:
            return None
        text = text[text.find(start)+len(start):]
        text = text[:text.find(end)]
        return text
    except:
        ...