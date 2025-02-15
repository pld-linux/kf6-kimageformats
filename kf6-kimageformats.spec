#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.11
%define		qtver		5.15.2
%define		kfname		kimageformats

Summary:	Image format plugins for Qt
Summary(pl.UTF-8):	Wtyczki formatów obrazów dla Qt
Name:		kf6-%{kfname}
Version:	6.11.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	4f035f9b0466e297bd95ee57eb53f820
URL:		https://kde.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6PrintSupport-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	libavif-devel >= 0.8.2
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel
BuildRequires:	ninja
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
This framework provides additional image format plugins for QtGui. As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

The following image formats have read-only support:
- DirectDraw Surface (dds)
- Gimp (xcf)
- OpenEXR (exr)
- Photoshop documents (psd)
- Sun Raster (ras)

The following image formats have read and write support:
- Encapsulated PostScript (eps)
- JPEG-2000 (jp2)
- Personal Computer Exchange (pcx)
- SGI images (rgb, rgba, sgi, bw)
- Softimage PIC (pic)
- Targa (tga): supports more formats than Qt's version
- XView (xv)

%description -l pl.UTF-8
Ten szkielet zapewnia dodatkowe wtyczki formatów obrazów dla QtGui.
Jako takie niest jest wymagany do budowania innego oprogramowania, ale
może być zależnością wymaganą do obsługi pewnych formatów przez
programy oparte na Qt.

Następujące formaty obrazów mają obsługę wyłącznie odczytu:
- DirectDraw Surface (dds)
- Gimp (xcf)
- OpenEXR (exr)
- dokumenty Photoshopa (psd)
- Sun Raster (ras)

Następujące formaty obrazów mają obsługę odczytu i zapisu:
- Encapsulated PostScript (eps)
- JPEG-2000 (jp2)
- Personal Computer Exchange (pcx)
- obrazy SGI (rgb, rgba, sgi, bw)
- Softimage PIC (pic)
- Targa (tga): więcej formatów, niż jest obsługiwanych w wersji Qt
- XView (xv)

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_ani.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_avif.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_hdr.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_eps.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_exr.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_jxl.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_kra.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_ora.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_pcx.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_pic.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_psd.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_ras.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_raw.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_rgb.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_tga.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_xcf.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_qoi.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_pfm.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_pxr.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_sct.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_dds.so
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_jp2.so
