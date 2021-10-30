# installation du module powershell requis
Install-WindowsFeature -name RSAT-AD-PowerShell

#Répertorier les APPLETS de commande disponibles
Get-Command -module ActiveDirectory

#Recherche de la date de création du compte utilisateur
Get-ADUser -Filter * -Properties whenCreated  | ft Name,SamAccountName,whenCreated

#Rechercher les comptes crées au cours des 5 derniers jours
$Days = 5
$Time = [DateTime]::Today.AddDays(-$Days)
Get-ADUser -Filter "(whenCreated -gt $Time)" -Properties whenCreated | ft Name,SamAccountName,whenCreated 

#Rechercher les comptes crées au cours des 30 derniers jours
$Days = 30
$Time = [DateTime]::Today.AddDays(-$Days)
Get-ADUser -Filter "(whenCreated -gt $Time)" -Properties whenCreated | ft Name,SamAccountName,whenCreated 


