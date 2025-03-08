# TODO libjxr
#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	heif		# HEIF image plugin

%define		kdeframever	6.11
%define		kf_ver		6.11.0
%define		qt_ver		6.6.0
%define		kfname		kimageformats

Summary:	Image format plugins for Qt
Summary(pl.UTF-8):	Wtyczki formatów obrazów dla Qt
Name:		kf6-%{kfname}
Version:	6.11.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	4f035f9b0466e297bd95ee57eb53f820
URL:		https://kde.org/
BuildRequires:	OpenEXR-devel >= 3.0
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6PrintSupport-devel >= %{qt_ver}
%{?with_tests:BuildRequires:	Qt6Test-devel >= %{qt_ver}}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-karchive-devel >= %{kf_ver}
BuildRequires:	libavif-devel >= 0.8.2
%{?with_heif:BuildRequires:	libheif-devel >= 1.10.0}
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel >= 0.9.4
BuildRequires:	libraw-devel >= 0.20.2
BuildRequires:	ninja
BuildRequires:	openjpeg2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	qt6-linguist >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6PrintSupport >= %{qt_ver}
Requires:	kf6-dirs
Requires:	kf6-karchive >= %{kf_ver}
Requires:	libavif >= 0.8.2
%{?with_heif:Requires:	libheif >= 1.10.0}
Requires:	libjxl >= 0.9.4
Requires:	libraw >= 0.20.2
#Obsoletes:	kf5-kimageformats < 6
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	%{?with_heif:-DKIMAGEFORMATS_HEIF=ON}

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
%if %{with heif}
%attr(755,root,root) %{qt6dir}/plugins/imageformats/kimg_heif.so
%endif
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
