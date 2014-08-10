Name:           sails
Version:        0.1
Release:        1%{?dist}
Summary:        Simulator for autonomous sailing boats

License:        GPLv3+
URL:            https://github.com/kragniz/sails
Source0:        https://github.com/kragniz/sails/archive/v0.1.tar.gz

BuildRequires:  cmake gtk3-devel librsvg2-devel
Requires:       gtk3 librsvg2

%description
Sails is a simulator designed to test the AI of autonomous sailing robots. It
emulates the basic physics of sailing a small single sail boat.

%prep
%autosetup

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/sails
%{_datadir}/%{name}/hull.svg
%{_datadir}/%{name}/sail.svg
%{_datadir}/%{name}/rudder.svg
%{_datadir}/applications/sails.desktop


%changelog
* Fri Aug  8 2014 Louis Taylor
- Initial version of the package
