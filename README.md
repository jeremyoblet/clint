# clint
This is my custom cross platform termional based on python

🌐 Fonctionnalité	🐧 Linux (bash)	💻 Windows CMD	⚡ PowerShell
Lister les fichiers/dossiers	ls [options]	dir	Get-ChildItem (alias gci)
Changer de dossier	cd <dossier>	cd <dossier>	Set-Location <dossier> (alias cd)
Afficher dossier courant	pwd	cd	Get-Location
Créer un dossier	mkdir <dossier>	mkdir <dossier>	New-Item -ItemType Directory <dossier>
Supprimer un fichier	rm <fichier>	del <fichier>	Remove-Item <fichier> (alias rm)
Supprimer un dossier	rm -r <dossier>	rmdir /S <dossier>	Remove-Item <dossier> -Recurse
Copier un fichier	cp src dst	copy src dst	Copy-Item src dst (alias cp)
Déplacer / renommer	mv src dst	move src dst	Move-Item src dst (alias mv)
Afficher le contenu d’un fichier	cat <fichier>	type <fichier>	Get-Content <fichier> (alias gc)
Lire un fichier page par page	less <fichier>	more <fichier>	Get-Content <fichier> -Wait
Rechercher du texte	grep "motif" fichier	find "motif" fichier	Select-String -Pattern "motif" (alias grep)
Redirection ﬂux standard	> / >>, 2>&1	> / >>, 2>&1	> / >>, ou Out-File, ErrorAction
Connexion remote	ssh user@host	ssh (via OpenSSH)	ssh user@host
Télécharger un URL	curl URL ou wget URL	curl URL (PowerShell compatible)	Invoke-WebRequest URL (alias curl)
Exécution de scripts	./script.sh	script.bat	.\script.ps1
Variables d’environnement	export VAR=value	set VAR=value	$Env:VAR = "value"
Afficher variables d’environnement	echo $VAR	echo %VAR%	echo $Env:VAR
Afficher utilisateur	whoami	whoami	whoami
Afficher processus	ps aux	tasklist	Get-Process (alias ps)
Tuer un processus	kill PID	taskkill /PID PID	Stop-Process -Id PID
Afficher flux réseau	netstat -tulpen	netstat -ano	Get-NetTCPConnection
Tester connectivité réseau	ping host	ping host	Test-Connection host
Mesurer temps d’exécution	time command	@echo off + echo %time% avant/après	Measure-Command { command }
Gestion des disques	df -h, du -sh ./	wmic logicaldisk get size,freespace,caption, dir	Get-PSDrive, Get-Volume
Monter un iso	mount -o loop fichier.iso /mnt	/mount (WSL) ou tiers	Mount-DiskImage -ImagePath fichier.iso
Archivage / compression	tar czf archive.tar.gz dossier	tiers + compact for NTFS	Compress-Archive -Path .\ -DestinationPath archive.zip
Extraire archive	tar xzf archive.tar.gz	tiers + expand	Expand-Archive archive.zip -DestinationPath .\
Éditeur de texte (CLI)	nano, vi, vim	notepad, edit	notepad <fichier>
Autocompletion	tab	tab	tab + Intellisense

copy [file or dir]
cut [file or dir]
paste [file or dir]



mysh/
├── main.py
├── completer.py
├── command_router.py
├── parser/                     # (plus tard) analyse syntaxique
│   ├── lexer.py
│   ├── parser.py
│   └── interpreter.py
├── context.py                  # variables, fonctions, env global
├── runtime/                    # moteur d’exécution
│   ├── evaluator.py
│   └── scope.py
└── commands/
    ├── make_file.py
    └── ...