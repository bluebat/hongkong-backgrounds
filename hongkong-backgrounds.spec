Summary: Backgrounds of HongKong
Name: hongkong-backgrounds
Version: 201712
Release: 1
License: CC-BY-SA
Group: User Interface/Desktops
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/bluebat/hongkong-backgrounds
BuildArch: noarch

%description
A background theme for HongKong:
126189-BayOfHK.jpg by pierreh from https://www.gnome-look.org/p/1082867/
night-2291750_1920.jpg by AndyLeung from https://pixabay.com/en/night-hong-kong-light-foggy-2291750/
vintage_hong_kong___fishing_junk_by_yesterdays_paper-dbcf0hh.jpg by Yesterdays-Paper from http://yesterdays-paper.deviantart.com/art/Vintage-Hong-Kong-Fishing-Junk-685983797/
16641980795_c5a9021a52_h.jpg by potaihse from https://visualhunt.com/f/photo/16641980795/c4582e6f75/
3488669309_c1b174c31f_o.jpg by dinesh_valke from https://visualhunt.com/f/photo/3488669309/ce40e6d026/

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md
%{_datadir}/backgrounds/hongkong
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Mon Dec 04 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 201712
- Initial package
