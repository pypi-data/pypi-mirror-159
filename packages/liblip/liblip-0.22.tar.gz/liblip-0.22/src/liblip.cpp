/**************************************************************************

 ***************************************************************************/
#include "liblipc.h"
#include <vector>
#include <map>
#include <unordered_map>
#include <iostream>
#define LIBEXP extern "C"

// Class to initialize global objects for procedural access
class Startup 
{
private:
  int glId; // STCInterpolant Id
  int sliId; // SLipInt Id
  int sliiId; // SLipIntInf Id
  int slilId; // SLipIntLp Id
public:
  Startup();
  ~Startup();
};

// global variables
// object/instance id
int objectId = -1; 

// instances of the interpolant class
std::unordered_map<int, STCInterpolant*> umgl;

// simple Lipschitz interpolant
std::map<int, SLipInt*> msli;

// simple Lipschitz interpolant
std::map<int, SLipIntInf*> mslii;

// SLipInt plus parameter p
std::map<int, SLipIntLp*> mslil;

// global lists of interpolant objects created at startup
Startup st;

// Lipschitz constant (not yet set)
double	GlobalLip=0;

LIBEXP int STCInterpolantInit()
{
	STCInterpolant* s = new STCInterpolant;
	umgl[++objectId] = s;
    return objectId;
}

LIBEXP void STCInterpolantDel( int id)
{
	if( id >= 0){
		umgl.erase( id);
	}
}


LIBEXP int SLipIntInit()
{
	int id = msli.size();
	SLipInt* s = new SLipInt;
	msli.insert( std::pair<int, SLipInt*>( id, s));
	return id;
}

LIBEXP void SLipIntDel( int id)
{
	if( id >= 0){
		msli.erase( id);
	}
}

LIBEXP int SLipIntInfInit()
{
	int id = mslii.size();
	// std::cout << "SLipIntInfInit num calls: " << numCall << " object id: " <<  id << std::endl;
	SLipIntInf* s = new SLipIntInf;
	mslii.insert( std::pair<int, SLipIntInf*>( id, s));
	return id;
}

LIBEXP void SLipIntInfDel( int id)
{
	// std::cout << "SLipIntInfDel, id: " << id << std::endl;
	if( id >= 0){
		mslii.erase( id);
	}
}


LIBEXP int SLipIntLpInit()
{
	int id = mslil.size();
	SLipIntLp* s = new SLipIntLp;
	mslil.insert( std::pair<int, SLipIntLp*>( id, s));
	return id;

}

LIBEXP void SLipIntLpDel( int id)
{
	if( id >= 0){
		mslil.erase( id);
	}
}


LIBEXP void	STCSetLipschitz( int id, double* x) 
{
	GlobalLip=*x;
}

LIBEXP int	STCBuildLipInterpolant( int id, int* Dim, int* Ndata, double* x, double* y)
{
	umgl.at( id)->SetData(*Dim,*Ndata,x,y);

	// Lipschitz constants live here
	if(GlobalLip<=0) {
		umgl.at( id)->DetermineLipschitz();
		umgl.at( id)->SetConstants();			// automatic
	} else
		umgl.at( id)->SetConstants(GlobalLip,*Dim+1);  // if it was specified

	umgl.at( id)->Construct();

	return umgl.at( id)->LastError();
//	if(gl.LastError()==ERR_LIP_LOW) cout << "Lipschitz const low or data coincide" << endl;
}

LIBEXP int	STCBuildLipInterpolantExplicit( int id, int* Dim, int* Ndata,  double* x, double* y)
{
	umgl.at( id)->SetData(*Dim,*Ndata,x,y);

	// Lipschitz constants live here
	if(GlobalLip<=0) {
		umgl.at( id)->DetermineLipschitz();
		umgl.at( id)->SetConstants();			// automatic, but slow
	} else
		umgl.at( id)->SetConstants(GlobalLip,*Dim+1);

	umgl.at( id)->ConstructExplicit();

	return umgl.at( id)->LastError();

//	if(umgl.at( id)->LastError()==ERR_LIP_LOW) cout << "Lipschitz const low or data coincide" << endl;
}

// the methods below are identical to the above, but use columnwise storage of matrices
LIBEXP int	STCBuildLipInterpolantColumn( int id, int* Dim, int* Ndata, double* x, double* y)
{
	umgl.at( id)->SetDataColumn(*Dim,*Ndata,x,y);

	// Lipschitz constants live here
	if(GlobalLip<=0) {
		umgl.at( id)->DetermineLipschitz();
		umgl.at( id)->SetConstants();			// automatic
	} else
		umgl.at( id)->SetConstants(GlobalLip,*Dim+1);  // if it was specified

	umgl.at( id)->Construct();

	return umgl.at( id)->LastError();
//	if(umgl.at( id)->LastError()==ERR_LIP_LOW) cout << "Lipschitz const low or data coincide" << endl;
}

LIBEXP int	STCBuildLipInterpolantExplicitColumn( int id, int* Dim, int* Ndata,  double* x, double* y)
{
	umgl.at( id)->SetDataColumn(*Dim,*Ndata,x,y);

	// Lipschitz constants live here
	if(GlobalLip<=0) {
		umgl.at( id)->DetermineLipschitz();
		umgl.at( id)->SetConstants();			// automatic, but slow
	} else
		umgl.at( id)->SetConstants(GlobalLip,*Dim+1);

	umgl.at( id)->ConstructExplicit();

	return umgl.at( id)->LastError();

//	if(umgl.at( id)->LastError()==ERR_LIP_LOW) cout << "Lipschitz const low or data coincide" << endl;
}


LIBEXP  double	STCValue( int id, double* x )
{
	return umgl.at( id)->Value(umgl.at( id)->Dim-1,x); // need to compute the slack variable 
}

LIBEXP  double	STCValueExplicit( int id, double* x )
{
	return umgl.at( id)->ValueExplicit(umgl.at( id)->Dim-1,x);
}


LIBEXP  void	STCFreeMemory( int id) {umgl.at( id)->FreeMemory();}

// additional functions
LIBEXP void LipIntConstruct( int id)
{
	umgl.at( id)->Construct();
}

LIBEXP double LipIntDetermineLipschitz( int id)
{
	return umgl.at( id)->DetermineLipschitz();
}

LIBEXP void LipIntFreeMemory( int id)
{
	umgl.at( id)->FreeMemory();
}

LIBEXP void LipIntSetConstants( int id)
{
	umgl.at( id)->SetConstants();
}

LIBEXP double LipIntValueExplicitDim( int id, int dim, double* x)
{
	return umgl.at( id)->ValueExplicit( dim, x);
}

LIBEXP double LipIntValueDim( int id, int dim, double* x)
{
	return umgl.at( id)->Value( dim, x);
}

LIBEXP void LipIntSetData( int id, int dim, int K, double* x, double* y, int test)
{
	umgl.at( id)->SetData( dim, K, x, y, test);
}


/*--------------------------------------------------------*/
/* interface to the members of SLipInt class */
LIBEXP double	LipIntValue( int id, int *Dim, int *Ndata, double* x, double* Xd,double* y,  double* Lipconst, int* Index)
{ return msli.find( id)->second->Value(*Dim, *Ndata, x, Xd, y, *Lipconst, Index); }

LIBEXP double	LipIntValueAuto( int id, int *Dim, int *Ndata, double* x,double* Xd, double* y, int* Index)
{ return msli.find( id)->second->Value(*Dim, *Ndata, x, Xd,y, Index); }

LIBEXP double	LipIntValueCons( int id, int* Dim, int* Ndata, int* Cons, double* x, double* Xd,double* y,  double* Lipconst, int* Index)
{ return msli.find( id)->second->ValueCons(*Dim, *Ndata, Cons, x, Xd, y, *Lipconst, Index); }

LIBEXP double	LipIntValueConsLeftRegion( int id, int* Dim, int* Ndata, int* Cons, double* x, double* Xd,double* y,  double* Lipconst, double* Region, int* Index)
{ return msli.find( id)->second->ValueConsLeftRegion( *Dim, *Ndata, Cons, x, Xd, y, *Lipconst, Region, Index); }

LIBEXP double	LipIntValueConsRightRegion( int id, int* Dim, int* Ndata, int* Cons, double* x, double* Xd,double* y,  double* Lipconst, double* Region, int* Index)
{ return msli.find( id)->second->ValueConsRightRegion( *Dim, *Ndata, Cons, x, Xd, y, *Lipconst, Region, Index); }


LIBEXP double	LipIntValueLocal( int id, int* Dim, int* Ndata, double* x, double* Xd,double* y)
{ 
	return msli.find( id)->second->ValueLocal(*Dim, *Ndata, x, Xd,y);
}

LIBEXP double	LipIntValueLocalCons( int id, int* Dim, int* Ndata,int* Cons, double* x, double* Xd,double* y)
{ return msli.find( id)->second->ValueLocalCons(*Dim, *Ndata, Cons, x, Xd,y); }

LIBEXP double	LipIntValueLocalConsLeftRegion( int id, int* Dim, int* Ndata,int* Cons, double* x, double* Xd,double* y, double* Region)
{ return msli.find( id)->second->ValueLocalConsLeftRegion(*Dim, *Ndata, Cons, x, Xd,y,Region); }

LIBEXP double	LipIntValueLocalConsRightRegion( int id, int* Dim, int* Ndata,int* Cons, double* x, double* Xd,double* y, double* Region)
{ return msli.find( id)->second->ValueLocalConsRightRegion(*Dim, *Ndata, Cons, x, Xd,y,Region); }


LIBEXP void	LipIntComputeLipschitz( int id, int* Dim, int* Ndata, double* x, double* y)
{  msli.find( id)->second->ComputeLipschitz(*Dim, *Ndata, x, y); }

LIBEXP void	LipIntComputeLocalLipschitz(  int id, int* Dim, int* Ndata, double* x, double* y)
{ 	
	msli.find( id)->second->ComputeLocalLipschitz(*Dim, *Ndata, x, y);
}

LIBEXP void	LipIntComputeLipschitzCV( int id, int* Dim, int* Ndata, double* Xd, double* y, double* T,
			int* type, int* Cons, double* Region, double *W)
{	msli.find( id)->second->ComputeLipschitzCV(*Dim,  *Ndata, Xd,  y,  T, *type,  Cons,  Region,  W); }

LIBEXP void	LipIntComputeLipschitzSplit( int id, int* Dim, int* Ndata, double* Xd, double* y, double* T, double* ratio,
			int* type, int* Cons, double* Region, double *W)
{	msli.find( id)->second->ComputeLipschitzSplit(*Dim,  *Ndata, Xd,  y,  T, *ratio, *type,  Cons,  Region,  W); }


LIBEXP void	LipIntSmoothLipschitz( int id, int* Dim, int* Ndata,  double* Xd, double* y, double* T,  double* LC, 
							  int* fW, int* fC, int* fR, double* W, int* Cons, double* Region)
{ // fR is 0, 1-left, 2-right
	msli.find( id)->second->SmoothLipschitz2internal(*Dim,*Ndata,Xd,  y,  T, 0,*fW, *fC, LC,  W, Cons, *fR, Region);
}


LIBEXP double	LipIntGetLipConst( int id) 
{ return msli.find( id)->second->MaxLipConst; }

LIBEXP void	LipIntGetScaling( int id, double *S) 
{	int i;
	for(i=0;i<msli.find( id)->second->NPTS;i++) 
	S[i]=msli.find( id)->second->Scaling[i]; 
}


LIBEXP int		LipIntComputeScaling( int id, int* Dim, int* Ndata, double* XData, double* YData)
{	return msli.find( id)->second->ComputeScaling(*Dim, *Ndata, XData,YData); }



LIBEXP void	ConvertXData( int id, int* dim, int* npts,  double* XData)
{    msli.find( id)->second->ConvertXData(*dim, *npts, XData); }

LIBEXP void	ConvertXDataAUX( int id, int* dim, int* npts,  double* XData, double *auxdata)
{    msli.find( id)->second->ConvertXData(*dim, *npts, XData,auxdata); }

LIBEXP int		LipIntVerifyMonotonicity( int id, int* dim, int* npts, int* Cons,  double* XData, double* YData, double* LC, double* eps)
{	return msli.find( id)->second->VerifyMonotonicity(*dim,*npts,Cons,XData,YData,*LC,*eps); }

LIBEXP int		LipIntVerifyMonotonicityLeftRegion( int id, int* dim, int* npts, int* Cons,  double* XData, double* YData, double* Region, double* LC, double* eps)
{	return msli.find( id)->second->VerifyMonotonicityLeftRegion(*dim,*npts,Cons,XData,YData,Region,*LC,*eps); }

LIBEXP int		LipIntVerifyMonotonicityRightRegion( int id, int* dim, int* npts, int* Cons,  double* XData, double* YData, double* Region, double* LC, double* eps)
{	return msli.find( id)->second->VerifyMonotonicityRightRegion(*dim,*npts,Cons,XData,YData,Region,*LC,*eps); }




/* interface to the members of SLipIntInf class ====================================== */
LIBEXP double	LipIntInfValue( int id, int* Dim, int* Ndata, double* x, double* Xd,double* y,  double* Lipconst, int* Index)
{
	return mslii.find( id)->second->Value(*Dim, *Ndata, x, Xd, y, *Lipconst, Index); 
	
}

LIBEXP double	LipIntInfValueAuto( int id, int* Dim, int* Ndata, double* x,double* Xd, double* y, int* Index)
{ return mslii.find( id)->second->Value(*Dim, *Ndata, x, Xd,y, Index); }

LIBEXP double	LipIntInfValueCons( int id, int* Dim, int* Ndata, int* Cons, double* x, double* Xd,double* y,  double* Lipconst, int* Index)
{ return mslii.find( id)->second->ValueCons(*Dim, *Ndata, Cons, x, Xd, y, *Lipconst, Index); }

LIBEXP double	LipIntInfValueConsLeftRegion( int id, int* Dim, int* Ndata, int* Cons, double* x, double* Xd,double* y,  double* Lipconst, double* Region, int* Index)
{ return msli.find( id)->second->ValueConsLeftRegion(*Dim, *Ndata, Cons, x, Xd, y, *Lipconst, Region, Index); }

LIBEXP double	LipIntInfValueConsRightRegion( int id, int* Dim, int* Ndata, int* Cons, double* x, double* Xd,double* y,  double* Lipconst, double* Region, int* Index)
{ return mslii.find( id)->second->ValueConsRightRegion(*Dim, *Ndata, Cons, x, Xd, y, *Lipconst, Region, Index); }


LIBEXP double	LipIntInfValueLocal( int id, int* Dim, int* Ndata, double* x, double* Xd,double* y)
{ return mslii.find( id)->second->ValueLocal(*Dim, *Ndata, x, Xd,y); }

LIBEXP double	LipIntInfValueLocalCons( int id, int *Dim, int* Ndata,int* Cons, double* x, double* Xd,double* y)
{ return mslii.find( id)->second->ValueLocalCons(*Dim, *Ndata, Cons, x, Xd,y); }

LIBEXP double	LipIntInfValueLocalConsLeftRegion( int id, int* Dim, int* Ndata,int* Cons, double* x, double* Xd,double* y, double* Region)
{ return mslii.find( id)->second->ValueLocalConsLeftRegion(*Dim, *Ndata, Cons, x, Xd,y,Region); }

LIBEXP double	LipIntInfValueLocalConsRightRegion( int id, int* Dim, int* Ndata,int* Cons, double* x, double* Xd,double* y, double* Region)
{ return mslii.find( id)->second->ValueLocalConsRightRegion(*Dim, *Ndata, Cons, x, Xd,y,Region); }


LIBEXP void	LipIntInfComputeLipschitz( int id, int* Dim, int* Ndata, double* x, double* y)
{  
	std::cout << "LipIntInfComputeLipschitz: " << id << std::endl;
	mslii.find( id)->second->ComputeLipschitz(*Dim, *Ndata, x, y); }

LIBEXP void	LipIntInfComputeLocalLipschitz(int id, int* Dim, int* Ndata, double* x, double* y)
{ 
	mslii.find( id)->second->ComputeLocalLipschitz(*Dim, *Ndata, x, y);
}

LIBEXP void	LipIntInfComputeLipschitzCV( int id, int* Dim, int* Ndata, double* Xd, double* y, double* T,
			int* type, int* Cons, double* Region, double *W)
{	mslii.find( id)->second->ComputeLipschitzCV(*Dim,  *Ndata, Xd,  y,  T, *type,  Cons,  Region,  W); }

LIBEXP void	LipIntInfComputeLipschitzSplit( int id, int* Dim, int* Ndata, double* Xd, double* y, double* T, double* ratio,
			int* type, int* Cons, double* Region, double *W)
{	mslii.find( id)->second->ComputeLipschitzSplit(*Dim,  *Ndata, Xd,  y,  T, *ratio, *type,  Cons,  Region,  W); }


LIBEXP void	LipIntInfSmoothLipschitz( int id, int* Dim, int* Ndata,  double* Xd, double* y, double* T,  double* LC, 
							  int* fW, int* fC, int* fR, double* W, int* Cons, double* Region)
{ // fR is 0, 1-left, 2-right
	mslii.find( id)->second->SmoothLipschitz2internal(*Dim,*Ndata,Xd,  y,  T, 0,*fW, *fC, LC,  W, Cons, *fR, Region);
}


LIBEXP double	LipIntInfGetLipConst( int id) 
{ return mslii.find( id)->second->MaxLipConst; }

LIBEXP void	LipIntInfGetScaling( int id, double *S) 
{	int i;
	for(i=0;i<msli.find( id)->second->NPTS;i++) 
	S[i]=mslii.find( id)->second->Scaling[i]; 
}


LIBEXP int		LipIntInfComputeScaling( int id, int* Dim, int* Ndata, double* XData, double* YData)
{	return mslii.find( id)->second->ComputeScaling(*Dim, *Ndata, XData,YData); }


LIBEXP int		LipIntInfVerifyMonotonicity( int id, int* dim, int* npts, int* Cons,  double* XData, double* YData, double* LC, double* eps)
{	return mslii.find( id)->second->VerifyMonotonicity(*dim,*npts,Cons,XData,YData,*LC,*eps); }

LIBEXP int		LipIntInfVerifyMonotonicityLeftRegion( int id, int* dim, int* npts, int* Cons,  double* XData, double* YData, double* Region, double* LC, double* eps)
{	return mslii.find( id)->second->VerifyMonotonicityLeftRegion(*dim,*npts,Cons,XData,YData,Region,*LC,*eps); }

LIBEXP int		LipIntInfVerifyMonotonicityRightRegion( int id, int* dim, int* npts, int* Cons,  double* XData, double* YData, double* Region, double* LC, double* eps)
{	return mslii.find( id)->second->VerifyMonotonicityRightRegion(*dim,*npts,Cons,XData,YData,Region,*LC,*eps); }


LIBEXP void	LipIntInfSmoothLipschitzSimp( int id, int* dim, int* npts,  double* XData, double* YData, double* TData,  double* LC)
{	mslii.find( id)->second->SmoothLipschitzSimp(*dim,*npts,XData,YData,TData,*LC);}

LIBEXP void	LipIntInfSmoothLipschitzSimpW( int id, int* dim, int* npts,  double* XData, double* YData, double* TData,  double *LC, double* W)
{	mslii.find( id)->second->SmoothLipschitzSimpW(*dim,*npts,XData,YData,TData,*LC,W);}

Startup::Startup()
{
	this->glId = STCInterpolantInit();
	this->sliiId = SLipIntInfInit();
	this->slilId = SLipIntLpInit();
	this->sliId = SLipIntInit();
	
}

Startup::~Startup()
{
	STCInterpolantDel( this->glId);
	SLipIntInfDel( this->sliiId);
	SLipIntLpDel( this->slilId);
	SLipIntDel( this->sliId);
}