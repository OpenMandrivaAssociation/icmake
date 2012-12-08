%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:        A hybrid between a 'make' utility and a 'shell script' language
Name:		icmake
Version:	7.16.00
Release:	1
License:	GPLv3
Group:		Development/Other
URL:		http://icmake.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_%{version}.orig.tar.gz

%description
Icmake is a hybrid between a 'make' utility and a 'shell script' language. 
Originally, it was written to provide a useful tool for automatic program 
maintenance and system administrative tasks on old MS-DOS platforms.

%package	doc
Group:		Development/Other
Summary:	Documentation for icmake

%description	doc
This package contains the documentation for icmake.

%prep
%setup -q

# set the correct LIBDIR path
sed -i -e "s:usr/lib:usr/%{_lib}:g" INSTALL.im

# fix executable perms in examples
pushd examples
for i in am backup bup defines ds ftpxfer idir \
	initialization keep killprog nesteddirectives r tolower
do
	chmod -x $i
done
popd

%build
%setup_compile_flags
./icm_bootstrap /

%install
./icm_install strip progs %{buildroot}
./icm_install scripts %{buildroot}
./icm_install skel %{buildroot}
./icm_install man %{buildroot}
./icm_install doc %{buildroot}
./icm_install docdoc %{buildroot}
./icm_install etc %{buildroot}

%files
%{_bindir}/ic*
%{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_docdir}/%{name}

%files doc
%{_docdir}/%{name}-doc


%changelog
* Mon Dec 19 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.16.00-1
+ Revision: 743738
- update to 7.16.00

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 7.15.00-1
+ Revision: 645237
- update to new version 7.15.00

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 7.12.5-2mdv2011.0
+ Revision: 611171
- rebuild

* Sat Dec 26 2009 Jérôme Brenier <incubusss@mandriva.org> 7.12.5-1mdv2010.1
+ Revision: 482330
- new version 7.12.5

* Sat Nov 21 2009 Jérôme Brenier <incubusss@mandriva.org> 7.12.3-1mdv2010.1
+ Revision: 467773
- import icmake

