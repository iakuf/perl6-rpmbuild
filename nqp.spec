#
# spec file for package nqp
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


Name:           nqp
Version:        2015.03
Release:        2.1.5
Summary:        Not Quite Perl
License:        Artistic-2.0
Group:          Development/Languages/Other
Url:            http://rakudo.org/
Source:         nqp-%{version}.tar.gz
Patch1:         usenqplibdir.diff
BuildRequires:  moarvm-devel
Requires:       moarvm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is "Not Quite Perl" -- a compiler for quickly generating PIR
routines from Perl6-like code.

%prep
%setup -q
%patch1
sed -i -e 's!@prefix@/lib/MAST!%{_libdir}/moar/MAST!g' tools/build/Makefile-Moar.in
sed -i -e 's!^NQP_LANG_DIR *=.*!NQP_LANG_DIR    = %{_libdir}/moar/languages/nqp!' tools/build/Makefile-common.in

%build
perl Configure.pl --backends=moar --prefix=%{_usr} 
make %{?_smp_mflags}

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS LICENSE
%{_bindir}/*
%{_libdir}/moar/languages/nqp

%changelog
* Fri Aug 22 2015 iakuf@163.com
- initial revision
