# final

- `output`: permite especificar todo o output exatamente como deve ser
  observado na saída do programa
- `match`: permite descrever todo o output através de uma regex que casar
  perfeitamente com a saída do programa
- `session`: permite descrever o output por partes; na prática é apenas um
  slicing da string completa que compõe a saída, facilitando a escrita e
  melhorando sua legibilidade; por ora, apenas partes `in` e `out` podem
  ser usadas para especificar, respectivamente, partes da entrada e da
  saída; no futuro, o plano é suportar também partes `mat` para especificar
  uma parte de saída como uma regex; e `tok` para indicar que uma parte de
  saída como um token que pode ser precedido ou seguido por qualquer trecho
  de string; 
- `tokens`: permite descrever o output como uma sequência de tokens
  (pedaços de strings) que devem ser observadas na saída, mas que não são
  um slicing do output; os _tokens_ podem ser precedidos, separados ou
  continuados por quaisquer outras strings;

# Interactive specification of tests

1. a cláusula `parts` (sem o uso de outras cláusulas) permite
   especificar partes independentes da saída de forma que o teste
   ignore tudo que estiver além dessas partes na saída do
   programa sendo testado; além disso, o formato permite
   intercalar as partes `in` e `out`, deixando o teste mais
   legível e, portanto, mais fáceis de escrever/manter para o
   aluno; as partes são verificadas estritamente, incluindo
   espaços, pontuação, outros caracteres, etc; o teste exige a
   presença de todas as partes e ignora todo o restante; esta é a
   semântica default de `parts`; requer cuidado com espaços nas
   strings `out` que serão exigidos;

    - parts:
        - out: "num 1?"
        - in: "2\n"
        - out: "num 2?"
        - in: "3\n"
        - out: "div = 0.67"

    re.match(".*[parte1].*[parte2].*[parte3].*[parte4].*", saida)


2. um teste com `parts` e com `strict: true` especifica que a
   saída esperada do teste é a exata concatenação das partes
   `out`; o texto de cada parte em si é livre (espaços,
   pontuação, etc) e será verificado estritamente; o mesmo
   cuidado com os espaços nas partes é necessário;

    - strict: true
      parts:
        - out: "num 1? "
        -  in: "2"
        - out: "num 2? "
        -  in: "3"
        - out: "---\n"
        - out: "div = 0.67\n"
        - out: "---\n"

    re.match([parte1][parte2][parte3][parte4][parte5], saida)

3. o uso de `tokens` permite especificar uma simples sequência de
   tokens independentes que devem ser confirmados na saída, na
   ordem dada e exatamente como são escritos; a propriedade
   `tokens` é no nível do teste e não dentro de `parts`; não se
   pode usar partes `out` no mesmo teste que tenha `tokens`; o
   valor de `tokens` deve ser uma lista de strings; se os tokens
   não tiverem espaços, a propriedade pode ser escrita como uma
   única string, usando espaços como separadores; (deve ser
   necessário tratar as strings com re.escape() para evitar que
   alguns detalhes e/ou caracteres sejam tomados como
   especificações de expressões regulares); o texto dos tokens é
   procurado estritamente; entre os tokens são esperados
   boundaries e texto livre ("\\b.*\\b" como separador, ".*\\b"
   no início e "\\b.*" no final);

    - parts:
        - in: "2\n"
        - in: "3\n"
      tokens: ["div", "0.67"]


4. quero poder usar regexes no lugar dos tokens para ter tokens
   com variablidade; neste caso, as strings não serão processadas
   com re.escape(); isso requer mais atenção do usuário, já que
   caracteres simples podem ter significado especial tais como
   estes: ".*()[]"; este tipo de especificação é especialmente
   interessante para exigir limites de palavras "\b"  ou ignorar
   casas decimais pequenas de números de ponto flutuante (ver
   abaixo), etc; também não permite usar partes do tipo `out`;

    re.match(stdout, match_spec)

    - parts:
        - in: "2"
        - in: "3"
      tokens-regex: ["\bdiv\b", "\b0.6"]


5. por fim, quero poder especificar uma regex detalhada, única
   para fazer um match completo do output; nesse caso, também, a
   string não deve ser processada com re.escape(), para que
   possamos usar as facilidades de re na especificação; também
   não permite usar partes `out`;

    re.match(stdout, match_spec)

    - parts:
        - in: "2\n"
        - in: "3\n"
      match: ".*\bdiv\b.*\b0.6.*"

