%define snap rc1
Summary:	MythTV Themes
Summary(pl.UTF-8):	Motywy dla MythTV
Name:		myththemes
Version:	0.22
Release:	0.%{snap}.2
License:	GPL v2
Group:		Themes
Source0:	%{name}-%{version}%{snap}.tar.bz2
# Source0-md5:	bb6773c2e24979c718f6ec6a7b551eaf
BuildRequires:	libmyth-devel >= 0.22
BuildRequires:	qt4-qmake
Requires:	mythtv-frontend >= %{version}
BuildArch:	noarch
# ExclusiveArch is because it's no point of building these on archidectures which don't have mythtv itself
ExclusiveArch:	%{ix86} %{x8664} ppc noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of themes for MythTV that used to be
distributed in the main download: Iulius, Minimalist-wide, Titivillus,
Titivillus-OSD.

%description -l pl.UTF-8
Ten pakiet zawiera motywy dla MythTV, wcześniej rozprowadzane wraz z
głównym pakietem: Iulius, Minimalist-wide, Titivillus, Titivillus-OSD.

%prep
#%setup -q %{SOURCE0}
%setup -q -n %{name}-%{version}%{snap}

%build
%configure
qmake-qt4 myththemes.pro \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/mythtv/themes/Graphite
%{_datadir}/mythtv/themes/Iulius-OSD
%{_datadir}/mythtv/themes/Mono-OSD
%{_datadir}/mythtv/themes/Mythbuntu
%{_datadir}/mythtv/themes/Retro-OSD
%{_datadir}/mythtv/themes/Titivillus-OSD
%{_datadir}/mythtv/themes/blueosd
%{_datadir}/mythtv/themes/metallurgy
