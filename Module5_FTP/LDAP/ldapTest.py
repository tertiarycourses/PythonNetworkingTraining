from ldap3 import Server, Connection, ALL

server = Server('ipa.demo1.freeipa.org', get_info=ALL)
conn = Connection(server, auto_bind=True)
#print(conn)
print(server.info)