#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : ade
Version  : 0.1.1d
Release  : 1
URL      : https://github.com/opencv/ade/archive/v0.1.1d.tar.gz
Source0  : https://github.com/opencv/ade/archive/v0.1.1d.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: ade-data = %{version}-%{release}
Requires: ade-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : googletest-dev

%description
# ADE Framework
## Intro
ADE Framework is a graph construction, manipulation, and processing
framework.  ADE Framework is suitable for organizing data flow
processing and execution.

%package data
Summary: data components for the ade package.
Group: Data

%description data
data components for the ade package.


%package dev
Summary: dev components for the ade package.
Group: Development
Requires: ade-data = %{version}-%{release}
Provides: ade-devel = %{version}-%{release}

%description dev
dev components for the ade package.


%package license
Summary: license components for the ade package.
Group: Default

%description license
license components for the ade package.


%prep
%setup -q -n ade-0.1.1d

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548787423
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1548787423
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ade
cp LICENSE %{buildroot}/usr/share/package-licenses/ade/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/ade/adeConfig.cmake
/usr/share/ade/adeConfigVersion.cmake
/usr/share/ade/adeTargets-relwithdebinfo.cmake
/usr/share/ade/adeTargets.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/ade/communication/callback_connector.hpp
/usr/include/ade/communication/comm_buffer.hpp
/usr/include/ade/communication/comm_interface.hpp
/usr/include/ade/edge.hpp
/usr/include/ade/execution_engine/backend.hpp
/usr/include/ade/execution_engine/executable.hpp
/usr/include/ade/execution_engine/execution_engine.hpp
/usr/include/ade/graph.hpp
/usr/include/ade/graph_listener.hpp
/usr/include/ade/handle.hpp
/usr/include/ade/helpers/search.hpp
/usr/include/ade/helpers/subgraphs.hpp
/usr/include/ade/memory/alloc.hpp
/usr/include/ade/memory/memory_access_listener.hpp
/usr/include/ade/memory/memory_accessor.hpp
/usr/include/ade/memory/memory_descriptor.hpp
/usr/include/ade/memory/memory_descriptor_ref.hpp
/usr/include/ade/memory/memory_descriptor_view.hpp
/usr/include/ade/memory/memory_types.hpp
/usr/include/ade/metatypes/metatypes.hpp
/usr/include/ade/node.hpp
/usr/include/ade/passes/check_cycles.hpp
/usr/include/ade/passes/communications.hpp
/usr/include/ade/passes/pass_base.hpp
/usr/include/ade/passes/topological_sort.hpp
/usr/include/ade/passmanager.hpp
/usr/include/ade/typed_graph.hpp
/usr/include/ade/typed_metadata.hpp
/usr/include/ade/util/algorithm.hpp
/usr/include/ade/util/assert.hpp
/usr/include/ade/util/chain_range.hpp
/usr/include/ade/util/checked_cast.hpp
/usr/include/ade/util/container_helper.hpp
/usr/include/ade/util/filter_range.hpp
/usr/include/ade/util/func_ref.hpp
/usr/include/ade/util/hash.hpp
/usr/include/ade/util/intrusive_list.hpp
/usr/include/ade/util/iota_range.hpp
/usr/include/ade/util/map_range.hpp
/usr/include/ade/util/math.hpp
/usr/include/ade/util/md_cast.hpp
/usr/include/ade/util/md_io.hpp
/usr/include/ade/util/md_size.hpp
/usr/include/ade/util/md_span.hpp
/usr/include/ade/util/md_view.hpp
/usr/include/ade/util/memory_range.hpp
/usr/include/ade/util/range.hpp
/usr/include/ade/util/range_iterator.hpp
/usr/include/ade/util/tuple.hpp
/usr/include/ade/util/type_traits.hpp
/usr/include/ade/util/zip_range.hpp
/usr/lib/*.a

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ade/LICENSE
