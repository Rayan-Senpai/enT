import os
import marshal

os.system('clear')
kontol = input(' [×] Masukan file : ')
baca = open(kontol,'r').read()
memek = compile(baca,"", "exec")
encrypt = marshal.dumps(memek)
coli = open('enc_'+str(kontol), 'w')
coli.write('import marshal\n')
coli.write('exec(marshal.loads('+repr(encrypt)+'))')
print(' [✓] Yes file telah di ecrypt -> enc_'+str(kontol))

