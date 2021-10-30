#git init
#.\gitconfig.ps1
git config --global user.name "Ousmana Traore"
git config --global user.email "traoreosman@yahoo.fr"
$filename = ".git"
$test = Test-Path -Path $filename
if($test -eq $True ){
Write-Host "Le repertoire $filename existe deja! " 
} else {
Write-Host "Le repertoire $filename  est absent..."
git init
}
#Test de la présence du repo cloné
$fichier = "asrs"
$test_fichier = Test-Path -Path $fichier
# $test_remote = "git remote -v"
$clone= "https://github.com/OusmanaTraore/asrs.git"


if($test_fichier -eq $True){

    Set-Location $fichier 
    Write-Host " Entree repo existant..."
    git remote -v
    Set-Location ..
    Write-Host " Sortie repo ..."
}else{
    Write-Host " Creation du repo clone..."
    Write-Host "Le clone $clone est absent"
    git clone $clone
    Write-Host "================================"
    Set-Location $fichier
    git remote -v    
}
#region Commit et push sur Git
git status
git fetch
$fichier_commit = Read-Host "Entrez les fichiers à commiter "
git add --$fichier_commit
git status
$commi = Read-Host "Entrez votre commit"
git status
git commit -m $commi
git status
git push -u origin master
#endregion