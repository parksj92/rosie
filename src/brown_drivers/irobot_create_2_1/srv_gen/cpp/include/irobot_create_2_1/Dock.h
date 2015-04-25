/* Auto-generated by genmsg_cpp for file /home/rbtying/humanoids/src/brown_drivers/irobot_create_2_1/srv/Dock.srv */
#ifndef IROBOT_CREATE_2_1_SERVICE_DOCK_H
#define IROBOT_CREATE_2_1_SERVICE_DOCK_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace irobot_create_2_1
{
template <class ContainerAllocator>
struct DockRequest_ {
  typedef DockRequest_<ContainerAllocator> Type;

  DockRequest_()
  {
  }

  DockRequest_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::irobot_create_2_1::DockRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::DockRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DockRequest
typedef  ::irobot_create_2_1::DockRequest_<std::allocator<void> > DockRequest;

typedef boost::shared_ptr< ::irobot_create_2_1::DockRequest> DockRequestPtr;
typedef boost::shared_ptr< ::irobot_create_2_1::DockRequest const> DockRequestConstPtr;



template <class ContainerAllocator>
struct DockResponse_ {
  typedef DockResponse_<ContainerAllocator> Type;

  DockResponse_()
  : success(false)
  {
  }

  DockResponse_(const ContainerAllocator& _alloc)
  : success(false)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;


  typedef boost::shared_ptr< ::irobot_create_2_1::DockResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::irobot_create_2_1::DockResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DockResponse
typedef  ::irobot_create_2_1::DockResponse_<std::allocator<void> > DockResponse;

typedef boost::shared_ptr< ::irobot_create_2_1::DockResponse> DockResponsePtr;
typedef boost::shared_ptr< ::irobot_create_2_1::DockResponse const> DockResponseConstPtr;


struct Dock
{

typedef DockRequest Request;
typedef DockResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Dock
} // namespace irobot_create_2_1

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::DockRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::DockRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::DockRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::irobot_create_2_1::DockRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::DockRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/DockRequest";
  }

  static const char* value(const  ::irobot_create_2_1::DockRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::DockRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::DockRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::DockRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::DockResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::irobot_create_2_1::DockResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::irobot_create_2_1::DockResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const  ::irobot_create_2_1::DockResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::irobot_create_2_1::DockResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/DockResponse";
  }

  static const char* value(const  ::irobot_create_2_1::DockResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::irobot_create_2_1::DockResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool success\n\
\n\
";
  }

  static const char* value(const  ::irobot_create_2_1::DockResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::irobot_create_2_1::DockResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::DockRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DockRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::irobot_create_2_1::DockResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DockResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<irobot_create_2_1::Dock> {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const irobot_create_2_1::Dock&) { return value(); } 
};

template<>
struct DataType<irobot_create_2_1::Dock> {
  static const char* value() 
  {
    return "irobot_create_2_1/Dock";
  }

  static const char* value(const irobot_create_2_1::Dock&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::DockRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const irobot_create_2_1::DockRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::DockRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Dock";
  }

  static const char* value(const irobot_create_2_1::DockRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<irobot_create_2_1::DockResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const irobot_create_2_1::DockResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<irobot_create_2_1::DockResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "irobot_create_2_1/Dock";
  }

  static const char* value(const irobot_create_2_1::DockResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // IROBOT_CREATE_2_1_SERVICE_DOCK_H

