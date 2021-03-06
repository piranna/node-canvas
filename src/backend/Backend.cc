#include <string>

#include <nan.h>

#include "Backend.h"


Backend::Backend(std::string name, int width, int height)
  : name(name)
  , width(width)
  , height(height)
	, format(CAIRO_FORMAT_INVALID)
{}

Backend::~Backend()
{
  this->destroySurface();
}

void Backend::init(const Nan::FunctionCallbackInfo<v8::Value> &info) {
  int width  = 0;
  int height = 0;
  if (info[0]->IsNumber()) width  = Nan::To<uint32_t>(info[0]).FromMaybe(0);
  if (info[1]->IsNumber()) height = Nan::To<uint32_t>(info[1]).FromMaybe(0);

  Backend *backend = construct(width, height);

  backend->Wrap(info.This());
  info.GetReturnValue().Set(info.This());
}

void Backend::setCanvas(Canvas* _canvas)
{
  this->canvas = _canvas;
}


void Backend::recreateSurface()
{
  this->destroySurface();

  this->createSurface();
}

DLL_PUBLIC cairo_surface_t* Backend::getSurface() {
  if (!surface) createSurface();
  return surface;
}

void Backend::destroySurface()
{
  if(this->surface)
  {
    cairo_surface_destroy(this->surface);
    this->surface = NULL;
  }
}


std::string Backend::getName()
{
  return name;
}

int Backend::getWidth()
{
  return this->width;
}
void Backend::setWidth(int width)
{
	this->width = width;
	this->recreateSurface();
}

int Backend::getHeight()
{
  return this->height;
}
void Backend::setHeight(int height)
{
  this->height = height;
  this->recreateSurface();
}

cairo_format_t Backend::getFormat()
{
	return this->format;
}
void Backend::setFormat(cairo_format_t format)
{
	this->format = format;
	this->recreateSurface();
}

bool Backend::isSurfaceValid(){
  bool hadSurface = surface != NULL;
  bool isValid = true;

  cairo_status_t status = cairo_surface_status(getSurface());

  if (status != CAIRO_STATUS_SUCCESS) {
    error = cairo_status_to_string(status);
    isValid = false;
  }

  if (!hadSurface)
    destroySurface();

  return isValid;
}


BackendOperationNotAvailable::BackendOperationNotAvailable(Backend* backend,
  std::string operation_name)
  : backend(backend)
  , operation_name(operation_name)
{};

BackendOperationNotAvailable::~BackendOperationNotAvailable() throw() {};

const char* BackendOperationNotAvailable::what() const throw()
{
  std::string msg = "operation " + this->operation_name +
    " not supported by backend " + backend->getName();

  return msg.c_str();
};
