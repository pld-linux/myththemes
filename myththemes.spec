%define	_snap 20051221
%define	_rev 8332
%define	_rel 0.1
Summary:	MythTV Themes
Summary(pl):	Motywy dla MythTV
Name:		myththemes
Version:	0.19.0.%{_snap}
Release:	0.%{_rev}.%{_rel}
License:	GPL v2
Group:		Applications
#Source0:	http://www.mythtv.org/mc/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{_snap}.%{_rev}.tar.bz2
# Source0-md5:	7d9c18b4078eaeed06fb2167fde5e361
BuildRequires:	qmake
Requires:	mythtv
BuildArch:	noarch
# ExclusiveArch is because it's no point of building these on archidectures which don't have mythtv itself
ExclusiveArch:	%{ix86} %{x8664} ppc noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of themes for MythTV that used to be
distributed in the main download: Iulius, Minimalist-wide, Titivillus,
Titivillus-OSD.

%description -l pl
Ten pakiet zawiera motywy dla MythTV, wcze¶niej rozprowadzane wraz z
g³ównym pakietem: Iulius, Minimalist-wide, Titivillus, Titivillus-OSD.

%prep
%setup -q %{?_snap:-n %{name}}

%build
qmake myththemes.pro \
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
%{_datadir}/mythtv/themes/Iulius
%{_datadir}/mythtv/themes/Iulius-OSD
%{_datadir}/mythtv/themes/Minimalist-wide
%{_datadir}/mythtv/themes/MythCenter
%{_datadir}/mythtv/themes/Titivillus
%{_datadir}/mythtv/themes/Titivillus-OSD
%{_datadir}/mythtv/themes/isthmus
