spec:=ansible-collection-dellemc-openmanage

srpm:
	cp ./build_ignore.patch $(shell rpmbuild --eval %{_sourcedir})
	cp ./gpgkey-42550ABD1E80D7C1BC0BAD851285491434D8786F.gpg $(shell rpmbuild --eval %{_sourcedir})
	@set -e; rpmbuild -bs --define "_disable_source_fetch 0" $(spec)
ifdef outdir
	cp `rpmbuild --eval "%{_topdir}"`/SRPMS/* $(outdir)
endif
