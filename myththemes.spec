Summary:	MythTV Themes
Name:		myththemes
Version:	0.18
Release:	0.2
License:	GPL v2
Group:		Applications
Source0:	http://www.mythtv.org/mc/%{name}-%{version}.tar.bz2
# Source0-md5:	9fe1f509b9ab7e6696e4d9aa0724c81f
Requires:	mythtv
# exclusivearch is just because it's no point of building these on
# arches which don't have mythtv itself
ExclusiveArch:	%{ix86} %{x8664} ppc noarch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of themes for MythTV that used to be
distributed in the main download: Iulius, Minimalist-wide, Titivillus,
Titivillus-OSD.


%prep
%setup -q

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
%{_datadir}/mythtv/themes/Titivillus-OSD
%{_datadir}/mythtv/themes/Titivillus
%{_datadir}/mythtv/themes/Minimalist-wide
%{_datadir}/mythtv/themes/Iulius
