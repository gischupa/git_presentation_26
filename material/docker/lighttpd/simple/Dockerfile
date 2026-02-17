FROM lighttpd:latest
# Für ernste Projekte Versionsnummer statt "latest"

# Config ersetzen
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf

# Website kopieren
COPY index.html /var/www/html/index.html

# Nur Doku
EXPOSE 80

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
