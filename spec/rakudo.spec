#
# spec file for package rakudo
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rakudo
Version:        2015.03
Release:        1.1%{dist}
Summary:        Perl 6 implemenation that runs on Parrot
License:        Artistic-2.0
Group:          Development/Languages/Other
Url:            http://rakudo.org/
Source0:        rakudo-%{version}.tar.gz
BuildRequires:  moarvm-devel
BuildRequires:  nqp
Provides:       perl6 = %{version}-%{release}
Requires:       moarvm
Requires:       nqp >= 2015.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
AutoReqProv:	no 

%description
Rakudo Perl 6, or just Rakudo, is an implementation of the Perl 6 
specification that runs on the Moar virtual machine.

%prep
%setup -q
sed -i -e "s!nqp::backendconfig<prefix>!'%{_libdir}/moar'!" src/vm/moar/ModuleLoaderVMConfig.nqp
sed -i -e 's!^PERL6_LANG_DIR *=.*!PERL6_LANG_DIR = %{_libdir}/moar/languages/perl6!' tools/build/Makefile-common.in
sed -i -e 's!^M_LIBPATH *=.*!M_LIBPATH = %{_libdir}/moar/languages/nqp/lib!' tools/build/Makefile-Moar.in
echo %{_libdir}/moar/languages/nqp/lib

%build
perl Configure.pl --prefix=%{_usr} 
make %{?_smp_mflags}

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS LICENSE
%{_bindir}/*
%{_libdir}/moar/languages/perl6
%{_libdir}/moar/languages/nqp/lib/Perl6

%changelog
* Wed Aug 23 2015 FuKai iakuf@163.com
- initial revision
