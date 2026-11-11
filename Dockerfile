# Citizen Tech Shop :: Dockerfile INTENCIONALMENTE VULNERAVEL (treino para Trivy)
# [VULN] imagem base antiga e fora de suporte (muitas CVEs de SO e do Python)
FROM python:3.4

# [VULN] segredos embutidos em variaveis de ambiente da imagem
ENV DB_PASSWORD=SuperSecret123!
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# [VULN] ADD (em vez de COPY) e copia de todo o contexto, inclusive segredos
ADD . /app
WORKDIR /app

# [VULN] instala dependencias antigas/vulneraveis sem fixar/atualizar o SO
RUN pip install -r requirements.txt

# [VULN] processo roda como root (sem USER nao-privilegiado)
USER root

EXPOSE 5000
# [VULN] app em modo debug exposto
CMD ["python", "app.py"]
