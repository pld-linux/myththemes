
#%define fix 24635

Summary:	MythTV Themes
Summary(pl.UTF-8):	Motywy dla MythTV
Name:		myththemes
Version:	0.23.1
#Release:        fix%{fix}.1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	ftp://ftp.osuosl.org/pub/mythtv/%{name}-%{version}.tar.bz2
# Source0-md5:	7dc2588a3235f84a957909449a8bda88
BuildRequires:	libmyth-devel >= 0.22
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-qmake
BuildRequires:	which
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
%setup -q

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
%{_datadir}/mythtv/themes/Arclight
%{_datadir}/mythtv/themes/Childish
%{_datadir}/mythtv/themes/Graphite
%{_datadir}/mythtv/themes/Iulius-OSD
%{_datadir}/mythtv/themes/Mono-OSD
%{_datadir}/mythtv/themes/Mythbuntu
%{_datadir}/mythtv/themes/ProjectGrayhem-OSD
%{_datadir}/mythtv/themes/Retro-OSD
%{_datadir}/mythtv/themes/Titivillus-OSD
%{_datadir}/mythtv/themes/blueosd
%{_datadir}/mythtv/themes/blootube-osd
%{_datadir}/mythtv/themes/metallurgy
