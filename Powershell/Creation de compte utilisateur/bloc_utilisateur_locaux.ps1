# Etape1 ,création de fichier CSV 
$fichier = "C:\Users\admin_sys\workstation\asrs\Powershell\bloc_utilisateur.csv"
$CSV= Import-Csv $fichier
 foreach ($LINE in $CSV) {
     $NewUser = "$($LINE.USERNAME)"
     $NewPass = "$($LINE.PASSWORD)"
     $SecurePass=ConvertTo-SecureString -AsPlainText -Force -String "$NewPass"
     New-LocalUser -Name $NewUser -Password $SecurePass
 }