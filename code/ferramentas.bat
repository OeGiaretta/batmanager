@echo off
:options
cls
echo =====================
echo Menu Opcoes:
echo =====================
echo   1 - Ver Meu Ip
echo   2 - Testar Conexao Internet (ping 8.8.8.8)
echo   3 - Testar Chapeco - Embratel
echo   4 - Testar Chapeco - EntrenaNet
echo   5 - Limpar Impressao
echo   6 - Verificar Conexoes abertas
echo   7 - Reiniciar Computador p/Rede
echo   8 - Desligar Computador  p/Rede
echo   9 - Anular Desligamento  p/Rede
echo  10 - Enviar Menssagem     p/Rede
echo  11 - Remoto Ipconfig
echo  12 - Servico VNC - Status
echo  13 - Servico VNC - Parar
echo  14 - Servico VNC - Iniciar
echo  15 - Remoto Informacoes de Sistema
echo  16 - Verificar Sistema Operacional do Computador p/rede
echo  17 - Verificar usuario logado no Desktop
echo  18 - Instalar Software p/Rede
echo  19 - Desinstalar Software p/Rede
echo  20 - Listar Softwares Instalados p/Rede
echo  21 - Listar impressoras instaladas p/Rede
echo  22 - Descobrir MAC do usuario pelo ip
echo  23 - Verificar Sys_Op p/rede 2.0
echo  24 - Instalar impressora p/Rede
echo  25 - Visualizar Chave office
echo  26 - HDD ou SDD p/Rede
echo  27 - FlushDNS Remoto
echo  28 - RegisterDNS Remoto
echo  29 - Fechar programas p/Rede
echo  30 - Criar novo projeto JAVA
echo  31 - Gerar CPF
echo  32 - Validar CPF
echo  33 - Gerar CNPJ
echo  34 - Validar CNPJ


echo =====================
echo   X para sair
echo =====================
set /p input="Digite a opcao aqui: "

if "%input%"=="1" goto:ipconfig
if "%input%"=="2" goto:internet
if "%input%"=="3" goto:chapecowan1
if "%input%"=="4" goto:chapecowan2
if "%input%"=="5" goto:imp
if "%input%"=="6" goto:conexoes
if "%input%"=="7" goto:reiniciar
if "%input%"=="8" goto:desligar
if "%input%"=="9" goto:anular
if "%input%"=="10" goto:msg
if "%input%"=="11" goto:ripconfig
if "%input%"=="12" goto:statusvnc
if "%input%"=="13" goto:stopvnc
if "%input%"=="14" goto:startvnc
if "%input%"=="15" goto:rsisinfo
if "%input%"=="16" goto:sysop
if "%input%"=="17" goto:usersys
if "%input%"=="18" goto:remoteIns
if "%input%"=="19" goto:remoteUni
if "%input%"=="20" goto:remoteView
if "%input%"=="21" goto:printersRem
if "%input%"=="22" goto:macip
if "%input%"=="23" goto:indentbit
if "%input%"=="24" goto:impinst
if "%input%"=="25" goto:officekey
if "%input%"=="26" goto:viewdiks
if "%input%"=="27" goto:remflush
if "%input%"=="28" goto:remregister
if "%input%"=="29" goto:closeexe
if "%input%"=="30" goto:newproject
if "%input%"=="31" goto:gerarcpf
if "%input%"=="32" goto:validarcpf
if "%input%"=="33" goto:gerarcnpj
if "%input%"=="34" goto:validarcnpj

if "%input%"=="x" goto:exit

echo Este menu nao existe!
pause
goto:options

:ipconfig
ipconfig.exe
pause
goto:options

:internet
ping 8.8.8.8 -n 6
pause
goto:options

:chapecowan1
ping 189.2.122.225 -n 6
pause
goto:options

:chapecowan2
ping 177.10.162.201 -n 6
pause
goto:options

:imp
net stop spooler 
cd %systemroot%\system32\spool\PRINTERS
del /f /s *.SHD
del /f /s *.SPL 
net start spooler
pause
goto:options

:conexoes
netstat
pause
goto:options

:reiniciar
set /p input2="informe o ip ou nome: "
net use \\%input2% /USER:DOMAIN\administrador SENHA
shutdown -r -f -m \\%input2% -t 35 -c "Seu computador sera reiniciado"
pause
goto:options

:desligar
set /p input5="informe o ip: "
net use \\%input5% /USER:DOMAIN\administrador SENHA
shutdown -s -f -m \\%input5% -t 35 -c "Seu Computador sera Desligado"
pause
goto:options

:anular
set /p input8="informe o ip: "
shutdown -a -m \\%input8% 
pause
goto:options

rem Inicio do comando

:msg
set /p input9="Informe o IP: "
set input10=%input9%

for /f "usebackq delims=\ tokens=2" %%a in (`wmic /node:%input10% computersystem get username /value ^| findstr /r /v "^$"`) do (
  call :TrimUsername "%%a"
)

set /p input17="Digite a mensagem: "
msg /W /V /SERVER:%input9% %username% %input17%
pause

exit /b

:TrimUsername
set "fullusername=%~1"
set "username=%fullusername:*\=%"
exit /b
goto:options

rem Fim do Comando

:ripconfig
set /p input11="informe o ip ou nome: "
psexec \\%input11% ipconfig /all
pause
goto:options

:statusvnc
set /p input12="informe o ip ou nome: "
SC \\%input12% query uvnc_service
pause
goto:options

:stopvnc
set /p input13="informe o ip ou nome: "
SC \\%input13% stop uvnc_service
pause
goto:options

:startvnc
set /p input14="informe o ip ou nome: "
SC \\%input14% start uvnc_service
pause
goto:options

:rsisinfo
set /p input15="Informe o IP ou NOME: "
psexec \\%input15% systeminfo
pause
goto:options

:sysop
set /p input16="informe o ip ou NOME do Desktop: "
net use J: \\%input16%\c$ /USER:DOMAIN\administrador SENHA
J:
if exist "Program Files (x86)\" (echo 64 bits) else (echo 32 bits)
C:
net use J: /delete
pause
goto:options

:usersys
set /p input18="informe o ip ou NOME do Desktop: "
wmic /node:%input18% computersystem get username
pause
goto:options

:remoteIns
set /p input19="informe o ip ou NOME do Desktop: "
set /p input20="informe o nome do software: "
net use W: \\%input19%\c$\Users /USER:DOMAIN\administrador SENHA
W:
winget install %input20%
C:
net use W: /delete
pause
goto:options

:remoteUni
set /p input21="informe o ip ou NOME do Desktop: "
set /p input22="informe o nome do software: "
net use W: \\%input21%\c$\Users /USER:DOMAIN\administrador SENHA
W:
winget uninstall %input22%
C:
net use W: /delete
pause
goto:options

:remoteview
set /p input23="informe o ip ou NOME do Desktop: "
net use W: \\%input23%\c$\Users /USER:DOMAIN\administrador SENHA
W:
winget list
C:
net use W: /delete
pause
goto:options

:printersRem
set /p input24="informe o ip ou NOME do Desktop: "
wmic /node:%input24% printer get caption, Status, portname
pause
goto:options

:macip
set /p input25="informe o ip: "
wmic /node:%input25% computersystem get username
wmic /node:%input25% computersystem get model, name
arp -a %input25%
pause
goto:options

:indentbit
set /p input26="informe o ip ou nome do Desktop: "
wmic /node:%input26% /user:DOMAIN\administrador /password:SENHA os get osarchitecture
pause
goto:options

:impinst
set /p input27="Informe o ip do Desktop Destinatario:"
set /p input28="Informe o ip da impressora que deseja instalar:"
rundll32 printui.dll, PrintUIEntry /o /c\\%input27% /ip %input28%
pause
goto:options

:officekey
set /p input29="Informe o ip ou nome do Desktop Destinatario: "
wmic /node:%input29% path softwarelicensingservice get OA3xOriginalProductKey
pause
goto:options

:viewdiks
set /p input30="Informe o ip ou nome do Desktop Destinatario: "
psexec -h -i \\%input30% -s powershell.exe -command "Get-PhysicalDisk"
pause
goto:options

:remflush
set /p input31="Informe o ip ou nome do Desktop Destinatario: "
psexec \\%input31% -u DOMAIN\administrador -p SENHA -d -i ipconfig /flushdns 
echo Finalizado!
pause
goto:options

:remregister
set /p input32="Informe o ip ou nome do Desktop Destinatario: "
psexec \\%input32% -u DOMAIN\administrador -p SENHA -d -i ipconfig /register
echo Finalizado!
pause
goto:options

:closeexe
set /p input33="Informe o ip ou nome do Desktop Destinatario: "
psexec \\%input33% -s tasklist
set /p input34="Digite o .exe que deseja fechar (EX:notepad.exe): " 
psexec \\%input33% -u DOMAIN\administrador -p SENHA -d -i taskkill /F /IM %input34%
echo Software finalizado!
pause
goto:options

:newproject
setlocal enabledelayedexpansion
set /p input35="Onde voce gostaria de gerar o projeto? "
cd !input35!
echo Voce selecionou o caminho: 
pwd
pause

set /p input36="Digite o nome do novo projeto: "
echo Criando novo projeto...
call mvn archetype:generate -DgroupId=com.main -DartifactId=!input36! -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

set /p input37="Gostaria de abrir o novo projeto? Y/n: "
echo Abrindo projeto!!
if /I !input37!==y (
cd !input35!/!input36! && code .
echo Projeto aberto!!
exit
)
echo Programa Finalizado!
pause
goto:options

:gerarcpf
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "acao=gerar_cpf&pontuacao=true" https://www.4devs.com.br/ferramentas_online.php > temp.txt
set /p cpf=<temp.txt
echo.
echo CPF Gerado: %cpf%
pause
goto:options 

:validarcpf
set /p cpf=Digite o CPF para validar: 
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "acao=validar_cpf&txt_cpf=%cpf%" https://www.4devs.com.br/ferramentas_online.php > temp.txt
type temp.txt
pause
goto options

:gerarcnpj
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "acao=gerar_cnpj&pontuacao=true" https://www.4devs.com.br/ferramentas_online.php > temp.txt
set /p cnpj=<temp.txt
echo.
echo CNPJ Gerado: %cnpj%
pause
goto options

:validarcnpj
set /p cnpj=Digite o CNPJ para validar: 
curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "acao=validar_cnpj&txt_cnpj=%cnpj%" https://www.4devs.com.br/ferramentas_online.php > temp.txt
type temp.txt
pause
goto options

:exit
exit


rem SCAN M4yGOD-crtM.exaroton.me
rem nmap -sS -sU -p- -A -v -T4 --script "default,safe,vuln" -oA scan_completo scanme.nmap.org      =       Scan agressivo de portas
rem nmap -A -v -T4 <alvo> = Scan simples com maximo de informação.
rem nmap -sS -sT <alvo> = Scan Basico.