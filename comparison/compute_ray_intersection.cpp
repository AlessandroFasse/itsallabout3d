// g++ compute_ray_intersection.cpp  -std=c++17 -O3 -I ~/libigl/external/eigen/ -I ~/libigl/include/ -o compute_ray_intersection

#include <iostream>
#include <ctime>
#include <Eigen/Dense>
#include <igl/readPLY.h>

int main(){
    Eigen::MatrixXd vertices;
    Eigen::MatrixXi faces;

    igl::readPLY("test.ply", vertices, faces);
    std::cout << "Number of faces = " << faces.rows() << std::endl;
    Eigen::Vector3d origin(0,0,0);
    for(unsigned i=0; i<vertices.rows(); ++i){
        origin += vertices.row(i);
    }
    origin /= vertices.rows();

    for(unsigned i=0; i<vertices.rows(); ++i){
        vertices.row(i) -= origin;
    }
    
    Eigen::Vector3d vec(1,0,0);
    Eigen::Vector3d point(0,0,0);
    clock_t start = clock();

    double distance, d, lambda0, lambda1, det;
    Eigen::Vector3d a, e0, e1, result;
    distance =10e100;
    for(unsigned j=0; j<faces.rows(); ++j){
        a = point.transpose() - vertices.row(faces(j,0));
        e0 = vertices.row(faces(j,1)) - vertices.row(faces(j,0));
        e1 = vertices.row(faces(j,2)) - vertices.row(faces(j,0));
        det = (e0.cross(e1)).dot(-vec.transpose());
        if(abs(det) >= 0.001){
            lambda0 = (a.cross(e1)).dot(-vec.transpose());
            lambda0 /= det;
            if(lambda0 >=0 and lambda0 <= 1){
                lambda1 = (e0.cross(a)).dot(-vec.transpose());
                lambda1 /= det;
                if(lambda1 >= 0 and lambda1 <= 1 and lambda0 + lambda1 <= 1){
                    d = (e0.cross(e1)).dot(a);
                    d /= det; 
                    if(abs(d) < distance){
                        distance = abs(d);
                        result = point + d * vec;
                    }
                }
            }
        }
    }
    std::cout << "Finished in " << double(clock() - start)/CLOCKS_PER_SEC << " seconds" << std::endl;
    std::cout << result << std::endl;


}