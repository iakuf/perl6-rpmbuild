Name:           moarvm
Version:        2015.03
Release:        1.1%{dist}
Summary:        Short for "Metamodel On A Runtime", MoarVM is a virtual machine as a backend for NQP and then Rakudo Perl 6 at the top.

License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://moarvm.org
Source0:        http://moarvm.org/releases/MoarVM-%{version}.tar.gz
AutoReqProv:    no

BuildRequires:  readline-devel libtommath-devel libuv-devel sha-devel
BuildRequires:  perl(Pod::Usage) perl(ExtUtils::Command) perl(autodie)

%description
Short for "Metamodel On A Runtime", MoarVM is a virtual machine built
especially for Rakudo Perl 6 and the NQP Compiler Toolchain. MoarVM is a 
backend for NQP.
MoarVM already stands out amongst the various Rakudo and NQP compilation
targets by typically:

    Running the Perl 6 specification test suite fastest
    Having the lowest memory usage
    Having the best startup time
    Being fastest to build both NQP and Rakudo - and thus in theory your
        Perl 6 and NQP programs too!

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files for developing applications that use
%{name} (Metamodel On A Runtime).

%prep
%setup -q -n MoarVM-%{version}

%build
# modify Configure.pl so that the Fedora specific flags for cflags and ldflags
# will be written to the Makefile
sed -i -e "/^\$config{cflags}/ s#.*#\$config{cflags} = \"$RPM_OPT_FLAGS -fPIC\";#" Configure.pl


%{__perl} Configure.pl --prefix=%{_usr} --libdir=%{_libdir}
#%{__perl} Configure.pl --prefix=%{_usr} --libdir=%{_libdir} --has-libtommath \
# --has-libuv --has-sha --use-readline 
#%if 0%{?fedora} > 20
#                       --use-readline --has-libatomic_ops
#%else
#                       --use-readline
#%endif

make %{?_smp_mflags}


%install
%make_install

# Force permissions on shared versioned libs so they get stripped
# and will provided.
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libmoar.so

%files
%doc LICENSE CREDITS docs
%{_bindir}/moar

%{_datadir}/nqp/lib/MAST
%{_datadir}/pkgconfig/moar.pc
%{_libdir}/libmoar.so

%files devel
%{_includedir}/dyncall
%{_includedir}/moar
%{_includedir}/tinymt

%exclude %{_includedir}/linenoise
%exclude %{_includedir}/libtommath
%exclude %{_includedir}/sha1
%exclude %{_includedir}/libuv
%exclude %{_includedir}/msinttypes
%exclude %{_includedir}/libatomic_ops

%changelog
* Wed Aug 23 2015 FuKai iakuf@163.com
- initial revision
