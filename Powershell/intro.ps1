GEt-ExecutionPolicy -List

# $PROFILE | Get-Member -Type NoteProperty

$PROFILE 

#Création de profil
if (!(Test-Path $PROFILE)){
    New-Item -ItemType File -Path $PROFILE -Force -WhatIf
}

$HOME

# editer un profil
 notepad $PROFILE

 #Module
 Get-Command -Module SimplySql

 #Creation de Modules Directory pour l'utilisateur actuel
 New-Item -Type Directory -Path $HOME\Documents\PowerShell\Modules 

 #Trouver la liste des modules installés
 Get-Module -ListAvailable

 #Trouver la commande dans un module
 Get-Command -Module module-name

 #Importation du module
 Import-Module  module-name

 #Ajout de TESCmdlets 
 Import-Module C:\ps-test\TestCmdlets
 Import-Module C:\ps-test\TestCmdlets.dll

 #Chemin du module

 $env:PSModulePath

 #Alias
 Get-Alias
 Set-Alias
 # Création d'Alias
 New-Alias -Name gh -Value Get-Help

 #Export , Import d'Alias
 Export-Alias -Path "alias.csv"
 Import-Alias test.txt



#Process
Get-Process | Sort-Object -Property handles

Get-Process -Name mse*
Get-Process -Name ch* | Stop-Process 
Get-Process -Name g* 

#Calling.Net librairies
$Object = [System.DateTime]:: Now

$Object
#Ajout de 15 heures à la date du système
$Object.AddHours(15) 

Add-Type -AssemblyName System.ServiceProcess   -WhatIf

Get-Help ?
Get-Help -Name Format-Table
Format-Table ?
help Format-Table 

#function

function Get-Info
{
    param($ComputerName)
    Get-WmiObject -ComputerName $ComputerName -Class Win32_BIOS
}

Get-Info -ComputerName localhost
#location des modules importable par leurs noms au lieu du chemin
$env:PSModulePath -split ';'

#Déplacement de notre module a C:\Users\$env:username\Documents\WindowsPowerShell\Modules