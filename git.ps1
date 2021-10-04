#git init
#.\gitconfig.ps1
$filename = ".git"
$test = Write-Output "Test-Path -Path $filename"
if($test -eq "true" ){
Write-Host "Le répertoire de git initialisé déjà existant."
continue; 
} else {
git init
}
#region Commit et push sur Git
git status
$fichier = Read-Host "Entrez les fichiers à commiter "
git add $fichier
git status
$commi = Read-Host "Entrez votre commit"
git status
git commit -m $commi
git status
git push -u origin master
#endregion