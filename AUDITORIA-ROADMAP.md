# Roadmap de qualidade do perfil Lvc4br

Este plano prioriza evidências de qualidade que um recrutador consegue verificar: demonstração funcional, instruções reproduzíveis, testes, decisões técnicas explicadas e escopo honesto.

> As prioridades abaixo são um plano de trabalho, não afirmações de que todos os itens já foram executados. A avaliação informal do perfil deve ser atualizada conforme cada entrega for verificada.

## Prioridade 1 — Portfólio como porta de entrada

Repositório: [LV_Portfolio](https://github.com/Lvc4br/LV_Portfolio)

- [ ] Conferir todas as rotas e galerias em desktop e mobile.
- [ ] Verificar links externos, formulário, imagens e estados de carregamento/erro.
- [ ] Garantir que cada projeto indique estado real, tecnologias e contribuição pessoal.
- [ ] Acrescentar uma demonstração curta ou capturas consistentes para projetos que não possam ser testados diretamente.
- [ ] Executar localmente `npm test`, `npm run lint` e `npm run build`; registrar qualquer falha antes de publicar.
- [ ] Confirmar que variáveis `VITE_*` não contêm segredos e que as integrações opcionais falham sem interromper a página.

**Critério de conclusão:** navegação principal verificada, build e testes aprovados, links funcionais e nenhum projeto apresentado como concluído sem evidência.

## Prioridade 2 — Java Lab: demonstrar engenharia de software

Repositório: [Java-Lab](https://github.com/Lvc4br/Java-Lab)

- [ ] Executar testes e build localmente, além de conferir a última execução da CI.
- [ ] Testar o fluxo completo: catálogo → carregar exercício → editar cópia → enviar → mostrar saída/erro.
- [ ] Testar falhas de rede, timeout, endpoint indisponível e entradas inválidas.
- [ ] Incluir capturas ou GIF curto da aplicação em uso.
- [ ] Documentar claramente as limitações do executor externo e nunca enviar código sensível.

**Critério de conclusão:** fluxo demonstrável, erros compreensíveis, testes reproduzíveis e instruções que funcionem em uma instalação limpa.

## Prioridade 3 — Nexo Analytics: reduzir riscos antes de chamar de produção

Repositório: [nexo-analytics](https://github.com/Lvc4br/nexo-analytics)

- [ ] Confirmar a CI atual e executar testes da API e build do dashboard.
- [ ] Revisar limitação de requisições: limite em memória não é compartilhado entre múltiplas instâncias.
- [ ] Validar configuração de produção com PostgreSQL persistente, sessão segura e origens CORS restritas.
- [ ] Verificar HTTPS, proxy confiável, logs sem dados sensíveis e comportamento em falha de banco.
- [ ] Documentar backup, retenção, exclusão de eventos e procedimento de recuperação.
- [ ] Separar explicitamente métricas do tracker próprio das métricas externas da Vercel.

**Critério de conclusão:** checklist de implantação testado em ambiente controlado; até lá, descrever o Nexo como projeto em evolução, não como serviço de produção comprovado.

## Prioridade 4 — Technical Art Toolkit: validar dentro do Blender

Repositório: [Technical Art Toolkit](https://github.com/Lvc4br/Lvc4br/tree/main/Technical-Art-Toolkit)

- [ ] Informar versões do Blender/Python suportadas.
- [ ] Testar instalação, ativação e desativação do add-on em uma versão real do Blender.
- [ ] Validar cada ferramenta em uma cena de teste e registrar resultados esperados.
- [ ] Adicionar capturas de tela ou vídeo curto de cada funcionalidade.
- [ ] Manter testes de compilação como verificação básica, sem tratá-los como substitutos de testes no Blender.

**Critério de conclusão:** instalação reproduzível e demonstração de cada função em ambiente real.

## Prioridade 5 — Projetos acadêmicos e protótipos

Repositórios: [NSA 2.0](https://github.com/Lvc4br/NSA-teste), [Projetos PW — ETEC](https://github.com/Lvc4br/Projetos-PW-ETEC), [Aprendizado Escolar 2025](https://github.com/Lvc4br/Aprendizado-Escolar-2025) e exercícios da ETEC.

- [ ] Conferir os fluxos principais no navegador, em desktop e mobile.
- [ ] Corrigir erros funcionais observados sem apagar o histórico acadêmico.
- [ ] Manter dados simulados no NSA 2.0; não usar informações reais de alunos.
- [ ] Preservar soluções originais de exercícios e adicionar versões corrigidas separadas quando necessário.
- [ ] Distinguir claramente o trabalho individual do trabalho em grupo.
- [ ] Identificar protótipos antigos como arquivo/histórico e evitar duplicar destaque na página inicial.

**Critério de conclusão:** cada README explica objetivo, estado, execução, limitações e autoria/contribuições.

## Ordem recomendada

1. **LV_Portfolio:** é a primeira página que um recrutador tende a abrir.
2. **Java Lab:** oferece um fluxo de software fácil de demonstrar.
3. **Technical Art Toolkit:** diferencia o perfil pela combinação de programação e 3D.
4. **Nexo Analytics:** pode demonstrar API, dashboard e modelagem, depois da revisão de implantação.
5. **Projetos acadêmicos:** manter organizados e honestamente descritos, sem investir neles mais tempo do que nos projetos principais.

## Como medir a evolução

Não aumentar a nota apenas por adicionar badges ou documentação. Reavaliar com evidências:

- [ ] Build/testes passam em ambiente limpo.
- [ ] Demo ou capturas correspondem ao código atual.
- [ ] README tem instalação, comandos, arquitetura e limitações corretas.
- [ ] Links e deploy foram testados.
- [ ] Segurança foi avaliada conforme o risco real do projeto.
- [ ] É possível explicar as principais decisões técnicas e o que foi feito pessoalmente.

A nota geral é uma estimativa qualitativa para orientar melhorias, não uma certificação nem uma previsão de contratação.

## Entrega verificada — 29/10/2026

- [x] **LV Portfolio:** o loader inicial respeita a preferência de acessibilidade `prefers-reduced-motion`, concluindo sem executar a animação quando a pessoa prefere movimento reduzido.
- [x] **Teste automatizado:** adicionado teste para a preferência de movimento reduzido e outro para a limpeza do `requestAnimationFrame` ao desmontar o componente.
- [x] **CI do LV Portfolio:** lint, testes e build de produção passaram no workflow [40809280001](https://github.com/Lvc4br/LV_Portfolio/actions/runs/40809280001).

Essa entrega cobre o comportamento do loader. Ainda não representa uma validação visual completa do site em navegadores reais ou dispositivos móveis.
